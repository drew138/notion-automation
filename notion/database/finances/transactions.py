from typing import Dict, List, Any, Optional
from notion.client.client import Client
from datetime import datetime
import os


class Transactions:
    def __init__(self) -> None:
        self.client = Client()
        self.database_id = os.getenv("NOTION_TRANSACTIONS_DATABASE_ID", "")

    def read(
        self,
        created_after: Optional[datetime] = None,
    ) -> List[Dict[str, Any]]:

        created_after_representation = (
            (created_after.strftime("%Y-%m-%dT%H:%M:%S.") + "000Z")
            if created_after
            else ""
        )

        response: Dict[str, Any] = self.client.query_from_database(
            self.database_id,
            created_after_representation,
        )

        return [
            {
                "id": row["id"],
                "name": (
                    row["properties"]["Name"]["title"][0]["text"]["content"]
                    if len(row["properties"]["Name"]["title"]) > 0
                    else None
                ),
                "amount": row["properties"]["Amount"]["number"],
                "date": (
                    row["properties"]["Date"]["date"]["start"]
                    if row["properties"]["Date"]["date"]
                    else None
                ),
                "type": (
                    row["properties"]["Type"]["select"]["name"]
                    if row["properties"]["Type"]["select"] is not None
                    and "name" in row["properties"]["Type"]["select"]
                    else None
                ),
                "subscription": [
                    subscription["id"]
                    for subscription in row["properties"]["Subscription"]["relation"]
                ],
            }
            for row in response["results"]
        ]

    def write(
        self,
        name: str,
        amount: int,
        date: str,
        row_type: str,
        subscription_id: str,
    ) -> Dict[str, Any]:
        body = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Name": {"title": [{"text": {"content": name}}]},
                "Amount": {"type": "number", "number": amount},
                "Date": {"date": {"start": date}},
                "Type": {"select": {"name": row_type}},
                "Subscription": {"relation": [{"id": subscription_id}]},
            },
        }
        return self.client.append_to_database(body)
