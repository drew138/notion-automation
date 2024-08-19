from task.task import Task
from datetime import datetime
from notion.database.finances.subscriptions import Subscriptions
from notion.database.finances.transactions import Transactions


class AppendTransactionsDatabase(Task):
    def __init__(self) -> None:
        self.subscription_db = Subscriptions()
        self.transaction_db = Transactions()

    def run(self) -> None:
        current_date = datetime.now()
        subscriptions = self.subscription_db.read()
        for subscription in subscriptions:
            renewal_date = datetime.strptime(
                subscription["renewal_date"],
                "%Y-%m-%d",
            )
            if renewal_date <= current_date:
                # TODO: check if already exists
                self.transaction_db.write(
                    name=subscription["name"],
                    amount=subscription["amount"],
                    date=current_date.strftime("%Y-%m-%d"),
                    row_type="Expense",
                    subscription_id=subscription["id"],
                )
