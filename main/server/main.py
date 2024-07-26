from flask import Flask, render_template_string
import plotly.io as pio

app = Flask(__name__)


@app.route("/")
def index():

    graph_html = pio.to_html(fig, full_html=False)

    return render_template_string(
        """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Interactive Plotly Chart</title>
    </head>
    <body>
        {{ graph_html|safe }}
    </body>
    </html>""",
        graph_html=graph_html,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
