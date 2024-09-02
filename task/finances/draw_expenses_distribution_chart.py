from task.task import Task
from chart.pie import PieChart
from notion.database.finances.transactions import Transactions
import plotly.graph_objects as go
from collections import defaultdict
from datetime import datetime
import pytz
import os


class DrawExpensesDistributionChartTask(Task):
    def __init__(self) -> None:
        self.transaction_db = Transactions()
        self.pie = PieChart()
        self.pay_day = int(os.getenv("PAY_DAY", "1"))

    def run(self) -> None:

        counts = defaultdict(int)

        now = datetime.now()

        if now.day >= self.pay_day:
            month = now.month
        else:
            month = now.month - 1

        month_start_date = datetime(
            now.year,
            month,
            self.pay_day,
            0,
            0,
            0,
            0,
            pytz.UTC,
        )
        transactions = self.transaction_db.read(month_start_date)

        for transaction in transactions:
            if not transaction["amount"]:
                continue
            if transaction["type"] == "Expense":
                counts[transaction["name"]] += transaction["amount"]

        self.pie.add_chart(list(counts.keys()), list(counts.values()))

        date = datetime.now().strftime("%B %Y")
        self.pie.update_fig_layout(
            f"Expenses Distribution {date}",
        )

    def get_fig(self) -> go.Figure:
        return self.pie.get_fig()
