from typing import Dict, Any, List
from notion.client.client import Client
import os


class Subscriptions:
    def __init__(self) -> None:
        self.client = Client()
        self.database_id = os.getenv("NOTION_SUBSCRIPTIONS_DATABASE_ID", "")

    def read(self) -> List[Dict[str, Any]]:
        response = self.client.query_from_database(self.database_id)

        return [
            {
                "id": row["id"],
                "name": (
                    row["properties"]["Name"]["title"][0]["text"]["content"]
                    if len(row["properties"]["Name"]["title"]) > 0
                    else None
                ),
                "renewal_date": (
                    row["properties"]["Renewal Date"]["formula"]["date"]["start"]
                    if "date" in row["properties"]["Renewal Date"]["formula"]
                    else None
                ),
                "amount": row["properties"]["Amount"]["number"],
            }
            for row in response["results"]
        ]
