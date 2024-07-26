NOTION_API_KEY=secret_twXAnKjvnwG6Bn8ptSZMZ6JcyKFRyt6z340bjtaMZSN

curl 'https://api.notion.com/v1/pages' \
    -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \
    -H "Content-Type: application/json" \
    -H "Notion-Version: 2022-06-28" \
    --data '{
	"parent": { "database_id": "6b4602270be2451c8238ce472eba45ae" },
    "properties": {
        "Type": {
            "select": {
                "name": "Income"
            }
        },
        "Cost": {
            "type": "number",
            "number": 20
        },
        "Date": {
            "date": {
                "start": "2024-08-16"
            }
        },
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "nuevo"
                    }
                }
            ]
        },
        "Subscription": {
            "relation": [
                {
                    "id": "0ad1e8fa-ca39-4b7e-8021-7c871a698763"
                }
            ]
        }
    }
}'


