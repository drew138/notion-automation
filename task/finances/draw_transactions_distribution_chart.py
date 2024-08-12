from task.task import Task
from chart.pie import PieChart
from notion.database.finances.transactions import Transactions
import plotly.graph_objects as go
from collections import defaultdict
from datetime import datetime


class DrawTransactionsDistributionChartTask(Task):
    def __init__(self) -> None:
        self.transaction_db = Transactions()
        self.pie = PieChart()

    def run(self) -> None:

        counts = defaultdict(int)

        # TODO: read only current month transactions
        transactions = self.transaction_db.read()

        income = 0
        other = 0
        for transaction in transactions:
            if transaction["type"] == "Income":
                income += transaction["amount"]
            elif transaction["type"]:
                counts[transaction["type"]] += transaction["amount"]
                other += transaction["amount"]

        counts["Income"] = max(income - other, 0)

        self.pie.add_chart(list(counts.keys()), list(counts.values()))

        self.pie.update_fig_layout(
            datetime.now().strftime("%B %Y"),
            "Transaction Distribution",
        )

    def get_fig(self) -> go.Figure:
        return self.pie.get_fig()


DrawTransactionsDistributionChartTask().run()
