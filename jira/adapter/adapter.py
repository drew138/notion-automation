from jira.client.client import Client
from typing import Dict, List
import os


class Adapter:
    def __init__(self) -> None:
        self.jira_project = os.getenv("JIRA_PROJECT", "")
        self.story_points_custom_field = "customfield_10117"
        self.client = Client()

    def get_current_sprint_id(self) -> Dict:
        response = self.client.fetch_active_sprints()
        sprints = response["values"]
        if not sprints:
            raise Exception("No active sprints found.")
        current_sprint = sorted(sprints, key=lambda x: x["startDate"], reverse=True)[0]
        return {
            "id": current_sprint["id"],
            "name": current_sprint["name"],
            "startDate": current_sprint["startDate"],
            "endDate": current_sprint["endDate"],
        }

    def get_assigned_issues(self, sprint_id: int) -> List[Dict]:
        jql = f"project = {self.jira_project} AND assignee = currentUser() AND sprint = {sprint_id}"
        fields = [self.story_points_custom_field, "summary", "status"]
        response = self.client.fetch_issues(jql, fields)
        return [
            {
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "story_points": issue["fields"][self.story_points_custom_field],
                "url": f"{self.client.base_url}/browse/{issue['key']}",
            }
            for issue in response["issues"]
        ]

    def get_reviewer_issues(self, sprint_id: int) -> List[Dict]:
        jql = f"project = {self.jira_project} AND sprint = {sprint_id}"
        fields = [self.story_points_custom_field, "summary", "status"]
        response = self.client.fetch_issues(jql, fields)
        return [
            {
                "key": issue["key"],
                "summary": issue["fields"]["summary"],
                "story_points": issue["fields"][self.story_points_custom_field],
                "url": f"{self.client.base_url}/browse/{issue['key']}",
            }
            for issue in response["issues"]
        ]
