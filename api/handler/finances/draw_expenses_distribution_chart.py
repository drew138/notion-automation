import plotly.io as pio
from flask import render_template
from task.finances.draw_expenses_distribution_chart import (
    DrawExpensesDistributionChartTask,
)


def index():
    task = DrawExpensesDistributionChartTask()
    task.run()
    fig = task.get_fig()
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("chart.html", graph_html=graph_html)
