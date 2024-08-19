from task.task import Task
from datetime import datetime
from notion.database.finances.subscriptions import Subscriptions
from notion.database.finances.transactions import Transactions
import pytz


class AppendTransactionsDatabase(Task):
    def __init__(self) -> None:
        self.subscription_db = Subscriptions()
        self.transaction_db = Transactions()

    def run(self) -> None:
        current_date = datetime.now()
        subscriptions = self.subscription_db.read()

        now = datetime.now()
        today = datetime(
            now.year,
            now.month,
            now.day,
            0,
            0,
            0,
            0,
            pytz.UTC,
        )

        transactions = self.transaction_db.read(today)
        todays_subscription = set(
            (transaction["name"], transaction["amount"]) for transaction in transactions
        )

        for subscription in subscriptions:
            renewal_date = datetime.strptime(
                subscription["renewal_date"],
                "%Y-%m-%d",
            )
            if renewal_date <= current_date:

                key = (subscription["name"], subscription["amount"])
                if key in todays_subscription:
                    continue

                self.transaction_db.write(
                    name=subscription["name"],
                    amount=subscription["amount"],
                    date=current_date.strftime("%Y-%m-%d"),
                    row_type="Expense",
                    subscription_id=subscription["id"],
                )
