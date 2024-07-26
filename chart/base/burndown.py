import plotly.graph_objects as go


class Burndown:
    def __init__(
        self,
        title,
        start_date,
        end_date,
        total_amount,
        units,
        actual_dates,
        actual_values,
    ):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.total_amount = total_amount
        self.units = units
        self.actual_dates = actual_dates
        self.actual_values = actual_values

        self.fig = go.Figure()

    def _add_chart(self):
        self.fig.add_trace(
            go.Scatter(
                x=self.actual_dates,
                y=self.actual_values,
                name="Actual",
                line=dict(color="royalblue", width=4),
            )
        )
        self.fig.add_trace(
            go.Scatter(
                x=[self.start_date, self.end_date],
                y=[self.total_amount, 0],
                name="Projected",
                line=dict(color="royalblue", width=4, dash="dash"),
            )
        )

        self.fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            title=self.title,
            xaxis_title="Date",
            yaxis_title=self.units,
        )

    def get_fig(self):
        self._add_chart()
        return self.fig
