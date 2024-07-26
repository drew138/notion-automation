from plotly.subplots import make_subplots
import plotly.graph_objects as go
from graph.settings import PIE_COLORS


class Pie:
    def __init__(self, title, name, labels, values, hole=0.0):
        if len(labels) != len(values):
            raise ValueError("Labels and values must have the same length")

        if len(labels) > len(PIE_COLORS):
            raise ValueError(f"Too many labels, max is {len(PIE_COLORS)}")

        self.title = title
        self.name = name
        self.labels = labels
        self.values = values
        self.colors = PIE_COLORS[: len(labels)]
        self.hole = hole
        self.fig = make_subplots(
            rows=1,
            cols=1,
            specs=[[{"type": "domain"}]],
        )

    def _add_chart(self):
        self.fig.add_trace(
            go.Pie(
                labels=self.labels,
                values=self.values,
                name="",
                hoverinfo="label+percent+value",
                textinfo="label+percent+value",
                marker=dict(colors=self.colors),
            ),
            1,
            1,
        )

        self.fig.update_traces(hole=self.hole)

        self.fig.update_layout(
            title_text=self.title,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            annotations=[
                dict(
                    text=self.name,
                    x=0.18,
                    y=0.5,
                    font_size=20,
                    showarrow=False,
                ),
            ],
        )

    def get_fig(self):
        self._add_chart()
        return self.fig
