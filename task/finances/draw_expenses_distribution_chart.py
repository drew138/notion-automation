from task.task import Task
from chart.pie import PieChart
from notion.database.finances.transactions import Transactions
import plotly.graph_objects as go
from collections import defaultdict
from datetime import datetime


class DrawExpensesDistributionChartTask(Task):
    def __init__(self) -> None:
        self.transaction_db = Transactions()
        self.pie = PieChart()

    def run(self) -> None:

        counts = defaultdict(int)

        # TODO: read only current month transactions
        transactions = self.transaction_db.read()

        for transaction in transactions:
            if not transaction["amount"]:
                continue
            if transaction["type"] == "Expense":
                counts[transaction["type"]] += transaction["amount"]

        self.pie.add_chart(list(counts.keys()), list(counts.values()))

        date = datetime.now().strftime("%B %Y")
        self.pie.update_fig_layout(
            f"Expenses Distribution {date}",
        )

    def get_fig(self) -> go.Figure:
        return self.pie.get_fig()
