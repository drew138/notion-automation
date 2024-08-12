import plotly.io as pio
from flask import render_template
from task.work.draw_burndown_chart import DrawBurndownChartTask


def index():
    task = DrawBurndownChartTask()
    task.run()
    fig = task.get_fig()
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("chart.html", graph_html=graph_html)
