from typing import List, Dict, Any
import requests
import os


class Client:
    def __init__(self) -> None:
        self.token: str = os.getenv("NOTION_TOKEN", "")
        self.version: str = "2022-06-28"

    def _create_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorizationa": f"Bearer {self.token}",
            "Notion-Version": self.version,
        }

    def fetch_from_database(self, database_id: str) -> Any:
        headers = self._create_headers()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def append_to_database(self, row: Dict) -> Any:
        headers = self._create_headers()
        url = "https://api.notion.com/v1/pages"
        response = requests.get(url, headers=headers, json=row)
        response.raise_for_status()
        return response.json()

    def parse_budget_response(self, response: Dict) -> List[Dict[str, Any]]:
        return [
            {
                "id": row["properties"]["id"],
                "type": row["properties"]["Type"]["select"]["name"],
                "date": row["properties"]["Date"]["date"]["start"],
                "subscription": [
                    subscription["id"]
                    for subscription in row["properties"]["Subscription"]["relation"]
                ],
                "name": (
                    row["properties"]["Name"]["title"][0]["text"]["content"]
                    if len(row["properties"]["Name"]["title"]) > 0
                    else None
                ),
                "amount": row["properties"]["Amount"]["number"],
            }
            for row in response["results"]
        ]

    def parse_subscription_response(self, response: Dict[str, Any]) -> List[Dict]:
        return [
            {
                "id": row["properties"]["id"],
                "name": (
                    row["properties"]["Name"]["title"][0]["text"]["content"]
                    if len(row["properties"]["Name"]["title"]) > 0
                    else None
                ),
                "recurrence": row["properties"]["Recurrence"]["select"]["name"],
                "amount": row["properties"]["Amount"]["number"],
            }
            for row in response["results"]
        ]

    def create_budget_row(
        self,
        database_id: str,
        row_type: str,
        amount: int,
        date: str,
        name: str,
        subscription_id: str,
    ) -> Dict[str, Any]:
        return {
            "parent": {"database_id": database_id},
            "properties": {
                "Type": {"select": {"name": row_type}},
                "Cost": {"type": "number", "number": amount},
                "Date": {"date": {"start": date}},
                "Name": {"title": [{"text": {"content": name}}]},
                "Subscription": {"relation": [{"id": subscription_id}]},
            },
        }
