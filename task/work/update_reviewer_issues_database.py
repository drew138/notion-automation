from task.task import Task
from jira.database.database import Database
from notion.database.work.reviewer_issues import ReviewerIssues


class UpdateReviewerIssuesDatabaseTask(Task):
    def __init__(self) -> None:
        self.jira_db = Database()
        self.notion_reviewer_issues_db = ReviewerIssues()

    def run(self) -> None:
        sprint = self.jira_db.get_current_sprint()

        jira_issues = self.jira_db.get_reviewer_issues(sprint["id"])

        notion_issues = self.notion_reviewer_issues_db.read()

        current_sprint_issue_keys = [issue["key"] for issue in jira_issues]

        notion_issue_keys = [issue["key"] for issue in notion_issues]

        for notion_issue in notion_issues:
            if notion_issue["key"] not in current_sprint_issue_keys:
                self.notion_reviewer_issues_db.delete(notion_issue["id"])

        key_translator = {issue["key"]: issue["id"] for issue in notion_issues}

        for jira_issue in jira_issues:

            args = [
                jira_issue["key"],
                jira_issue["summary"],
                jira_issue["url"],
                jira_issue["assignee"]["emailAddress"],
                jira_issue["status"],
            ]

            if jira_issue["key"] in notion_issue_keys:
                self.notion_reviewer_issues_db.update(
                    key_translator[jira_issue["key"]], *args
                )
            else:
                self.notion_reviewer_issues_db.write(*args)


UpdateReviewerIssuesDatabaseTask().run()
