from typing import List
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class PieChart:
    def __init__(self) -> None:

        self.fig: go.Figure = make_subplots(
            rows=1,
            cols=1,
            specs=[[{"type": "domain"}]],
        )

    def add_chart(self, labels: List[str], values: List[int]) -> None:
        self.fig.add_trace(
            go.Pie(
                labels=labels,
                values=values,
                hoverinfo="label+percent+value",
                textinfo="label+percent+value",
                textfont=dict(color="white"),
                hoverlabel=dict(font=dict(color="white")),
            ),
            1,
            1,
        )

        self.fig.update_traces(hole=0.6)

    def update_fig_layout(self, name: str, title: str) -> None:

        self.fig.update_layout(
            title_text=title,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            annotations=[
                dict(
                    text=name,
                    x=0.5,
                    y=0.5,
                    font_size=20,
                    showarrow=False,
                ),
            ],
        )

    def get_fig(self) -> go.Figure:
        return self.fig