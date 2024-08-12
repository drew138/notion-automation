# Notion Automation

This project is a simple tool that helps to manage my notion finances
and work pages by automating some tasks regarding
database entries and data visualization.

## Environment Variables

### Jira Client

Currently found in the `jira/client/client.py` file.
It requires the following environment variables:

- `JIRA_BASE_URL`: base url of the jira workspace.
- `JIRA_ACCESS_TOKEN`: jira access token used to access the jira api.
  An api token can be generated in the jira settings.
  Then it should be passed through the
  following command to obtain this token: `echo -n <email>:<token> | base64`
- `JIRA_BOARD_ID`: id of the jira board. Obtainable through the
  browser url of the board.

### Jira Database

Currently found in the `jira/database/database.py` file.
It requires the following environment variables:

- `JIRA_PROJECT`: Obtainable through the browser url of the project.
  The url follows the following format
  `<base_url>/jira/software/c/projects/<jira_project>/boards/<jira_board_id>`.
- `JIRA_STORY_POINTS_CUSTOM_FIELD`: Field containing story points.
  This field can be searched using the following Jira api endpoint
  `https://mercadolibre.atlassian.net/rest/api/latest/field`.
- `JIRA_REVIEWER_CUSTOM_FIELD`: Field containing issue reviewer.
  This field can be searched using the following Jira api endpoint
  `https://mercadolibre.atlassian.net/rest/api/latest/field`.

### Main

Currently found in the `main/server/main.py` file.
It requires the following environment variables:

- `ROUTE`: name of the task being executed.
- `PORT`: Default port is 8080.

### Notion Client

Currently found in the `notion/client/client.py` file.
It requires the following environment variables:

- `NOTION_TOKEN`

### Notion Databases

Currently found in the
`notion/database/finances/subscriptions.py`,
`notion/database/finances/transactions.py`,
`notion/database/work/assigned_issues.py`
and `notion/database/work/reviewer_issues.py` files.
They requires the following environment variables correspondingly:

- `NOTION_SUBSCRIPTIONS_DATABASE_ID`
- `NOTION_TRANSACTIONS_DATABASE_ID`
- `NOTION_ASSIGNED_ISSUES_DATABASE_ID`
- `NOTION_REVIEWER_ISSUES_DATABASE_ID`

All of the above can be accesed in the page view of the database, using its url.
the url follows the following format: `https://www.notion.so/<database_id>?v=<view_id>`
