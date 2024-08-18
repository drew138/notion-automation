from jira.client.client import Client
from datetime import datetime, date
from typing import Dict, List, Optional
import os
import threading


class Database:
    def __init__(self) -> None:
        self.jira_project = os.getenv(
            "JIRA_PROJECT",
            "",
        )
        self.story_points_custom_field = os.getenv(
            "JIRA_STORY_POINTS_CUSTOM_FIELD",
            "",
        )
        self.reviewer_custom_field = os.getenv(
            "JIRA_REVIEWER_CUSTOM_FIELD",
            "",
        )
        self.date_format = "%Y-%m-%dT%H:%M:%S.%f%z"
        self.client = Client()

    def get_current_sprint(self) -> Dict:
        response = self.client.fetch_active_sprints()

        sprints = response["values"]

        if not sprints:
            raise Exception("No active sprints found.")

        current_sprint = sorted(
            sprints,
            key=lambda x: x["startDate"],
            reverse=True,
        )[0]

        return {
            "id": current_sprint["id"],
            "name": current_sprint["name"],
            "start_date": datetime.strptime(
                current_sprint["startDate"], self.date_format
            ).date(),
            "end_date": datetime.strptime(
                current_sprint["endDate"], self.date_format
            ).date(),
        }

    def get_assigned_issues(self, sprint_id: int) -> List[Dict]:
        conditions = [
            f"project = {self.jira_project}",
            f"sprint = {sprint_id}",
            "assignee = currentUser()",
        ]
        jql = " AND ".join(conditions)
        fields = [self.story_points_custom_field, "summary", "status"]
        response = self.client.fetch_issues(jql, fields)
        story_points = self.story_points_custom_field
        assigned_issues = [
            {
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "url": f"{self.client.base_url}/browse/{issue['key']}",
                "story_points": issue["fields"][story_points],
                "status": self._translate_status(
                    issue["fields"]["status"]["name"],
                ),
            }
            for issue in response["issues"]
        ]
        threads = []
        for assigned_issue in assigned_issues:
            t = threading.Thread(
                target=self._assign_completion_date,
                args=[assigned_issue],
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return assigned_issues

    def get_reviewer_issues(self, sprint_id: int) -> List[Dict]:
        id = self.reviewer_custom_field.split("_")[1]
        conditions = [
            f"project = {self.jira_project}",
            f"sprint = {sprint_id}",
            f"cf[{id}] = currentUser()",
        ]
        jql = " AND ".join(conditions)
        fields = ["assignee", "summary", "status"]
        response = self.client.fetch_issues(jql, fields)
        return [
            {
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "url": f"{self.client.base_url}/browse/{issue['key']}",
                "assignee": issue["fields"]["assignee"],
                "status": self._translate_status(
                    issue["fields"]["status"]["name"],
                ),
            }
            for issue in response["issues"]
        ]

    def _get_completion_date(
        self,
        issue_id: int,
        status: str,
    ) -> Optional[date]:
        done = "DONE"
        if status != done:
            return None

        response = self.client.fetch_issue_changelog(issue_id)

        changelog = response["values"]
        resolution_date = None
        for change in changelog:
            for item in change["items"]:
                if item["field"] == "status" and item["toString"].upper() == done:
                    resolution_date = change["created"]

        if resolution_date:
            resolution_date = datetime.strptime(
                resolution_date, self.date_format
            ).date()

        return resolution_date

    def _assign_completion_date(
        self,
        issue: Dict,
    ) -> Optional[date]:
        completion_date = self._get_completion_date(
            issue["key"],
            issue["status"],
        )
        issue["completion_date"] = completion_date

    # TODO: idk how but parameterize this sht
    def _translate_status(self, status: str) -> str:
        if status == "Tareas por hacer":
            return "TO DO"
        elif status == "En curso":
            return "IN PROGRESS"
        elif status == "TO VERIFY":
            return "TO VERIFY"
        elif status == "Finalizada":
            return "DONE"
        return "TO DO"
