from typing import Dict, List, Any
from notion.client.client import Client
import os


class ReviewerIssues:
    def __init__(self) -> None:
        self.client = Client()
        self.database_id = os.getenv("NOTION_REVIEWER_ISSUES_DATABASE_ID", "")

    def read(self) -> List[Dict[str, Any]]:
        response = self.client.query_from_database(self.database_id)

        return [
            {
                "id": row["id"],
                "key": (
                    row["properties"]["Key"]["title"][0]["text"]["content"]
                    if len(row["properties"]["Key"]["title"]) > 0
                    else None
                ),
                "summary": (
                    row["properties"]["Summary"]["rich_text"][0]["text"]["content"]
                    if len(row["properties"]["Summary"]["rich_text"]) > 0
                    else None
                ),
                "link": row["properties"]["Link"]["url"],
                "assignee": row["properties"]["Assignee"]["email"],
                "status": (
                    row["properties"]["Status"]["status"]["name"]
                    if row["properties"]["Status"]["status"]
                    else None
                ),
            }
            for row in response["results"]
        ]

    def write(
        self,
        key: str,
        summary: str,
        url: str,
        asignee: str,
        status: str,
    ) -> Dict[str, Any]:
        body = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Key": {"title": [{"text": {"content": key}}]},
                "Summary": {"rich_text": [{"text": {"content": summary}}]},
                "Link": {"url": url},
                "Assignee": {"email": asignee},
                "Status": {"status": {"name": status}},
            },
        }
        return self.client.append_to_database(body)

    def update(
        self,
        row_id: str,
        key: str,
        summary: str,
        url: str,
        asignee: str,
        status: str,
    ) -> Dict[str, Any]:
        body = {
            "properties": {
                "Key": {"title": [{"text": {"content": key}}]},
                "Summary": {"rich_text": [{"text": {"content": summary}}]},
                "Link": {"url": url},
                "Assignee": {"email": asignee},
                "Status": {"status": {"name": status}},
            },
        }
        return self.client.update_database_row(row_id, body)

    def delete(self, row_id: str) -> None:
        self.client.delete_database_row(row_id)
