import plotly.io as pio
from flask import render_template
from task.work.draw_completion_chart import DrawCompletionChartTask


def index():
    task = DrawCompletionChartTask()
    task.run()
    fig = task.get_fig()
    graph_html = pio.to_html(fig, full_html=False)
    return render_template("chart.html", graph_html=graph_html)
