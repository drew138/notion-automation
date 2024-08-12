from typing import Dict, Any
import os
import aiohttp
import asyncio


class Client:
    def __init__(self) -> None:
        self.base_url: str = "https://api.notion.com"
        self.token: str = os.getenv("NOTION_TOKEN", "")
        self.version: str = "2022-06-28"

    def _create_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": self.version,
        }

    def query_from_database(self, database_id: str) -> Any:
        headers = self._create_headers()
        url = f"{self.base_url}/v1/databases/{database_id}/query"

        async def fetch():
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url,
                    headers=headers,
                ) as response:
                    return await response.json()

        return asyncio.run(fetch())

    def append_to_database(self, body: Dict) -> Any:
        headers = self._create_headers()
        url = f"{self.base_url}/v1/pages"

        async def fetch():
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url,
                    headers=headers,
                    json=body,
                ) as response:
                    return await response.json()

        return asyncio.run(fetch())

    def update_database_row(self, row_id: str, body: Dict) -> Any:
        headers = self._create_headers()
        url = f"{self.base_url}/v1/pages/{row_id}"

        async def fetch():
            async with aiohttp.ClientSession() as session:
                async with session.patch(
                    url,
                    headers=headers,
                    json=body,
                ) as response:
                    return await response.json()

        return asyncio.run(fetch())

    def delete_database_row(self, row_id: str) -> Any:
        headers = self._create_headers()
        url = f"{self.base_url}/v1/pages/{row_id}"

        body = {
            "archived": True,
        }

        async def fetch():
            async with aiohttp.ClientSession() as session:
                async with session.patch(
                    url,
                    json=body,
                    headers=headers,
                ) as response:
                    return await response.json()

        return asyncio.run(fetch())
