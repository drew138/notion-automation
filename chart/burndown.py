import plotly.graph_objects as go
from typing import List
from datetime import date


class BurndownChart:
    def __init__(self) -> None:
        self.fig = go.Figure()

    def add_actual_chart(self, points: List[int], days: List[date]) -> None:
        self.fig.add_trace(
            go.Scatter(
                y=points,
                x=days,
                name="Actual",
                line=dict(
                    color="royalblue",
                    width=4,
                ),
            )
        )

    def add_ideal_chart(self, points: List[int], days: List[date]) -> None:
        self.fig.add_trace(
            go.Scatter(
                y=points,
                x=days,
                name="Ideal",
                line=dict(
                    color="crimson",
                    width=4,
                    dash="dash",
                ),
            )
        )

    def update_fig_layout(self, title: str) -> None:
        self.fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            title=dict(
                text=title,
                font=dict(
                    color="white",
                    size=20,
                    weight="bold",
                ),
            ),
            xaxis_title="Date",
            yaxis_title="Story Points",
            yaxis=dict(
                dtick=1,
                color="white",
            ),
            xaxis=dict(
                type="date",
                tickmode="linear",
                dtick="D1",
                tickformat="%Y-%m-%d",
                tickangle=-45,
                color="white",
            ),
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.5,
                xanchor="center",
                x=0.5,
                font=dict(color="white"),
            ),
        )

    def get_fig(self) -> go.Figure:
        return self.fig
