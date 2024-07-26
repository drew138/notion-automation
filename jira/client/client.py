import os
import requests

# search issues jira
# https://mercadolibre.atlassian.net/rest/api/3/search


# {
#     "jql": "project = MCRB AND assignee = currentUser() AND sprint in openSprints() AND key = MCRB-1013",
#     "fields": ["assignee", "customfield_10117", "summary", "customfield_14140"]
# }

# Story Points - customfield_10117
# Reviewer - customfield_14140
# End Date - customfield_12368

# board id must be passed
# https://mercadolibre.atlassian.net/rest/agile/1.0/board/10208/sprint?state=active


# issue in browser
# https://mercadolibre.atlassian.net/browse/<issue-id>


# fields in issues
# https://mercadolibre.atlassian.net/rest/api/latest/field


class Client:
    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL", "")
        self.token = os.getenv("JIRA_ACCESS_TOKEN", "")
        self.board_id = os.getenv("JIRA_BOARD_ID", "")  # 10208

    def _create_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorizationa": f"Basic {self.token}",
        }

    def fetch_issues(self, jql, fields):
        body = {"jql": jql, "fields": fields}
        headers = self._create_headers()
        url = f"{self.base_url}/rest/api/3/search"
        response = requests.get(url, json=body, headers=headers)
        response.raise_for_status()
        return response.json()

    def fetch_active_sprints(self):
        headers = self._create_headers()
        url = (
            f"{self.base_url}/rest/agile/1.0/board/{self.board_id}/sprint?state=active"
        )
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def fetch_issue_changelog(self, issue_id):
        headers = self._create_headers()
        url = f"{self.base_url}/rest/api/3/issue/{issue_id}/changelog"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
