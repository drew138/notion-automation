from task.task import Task
from jira.database.database import Database
from datetime import datetime, timedelta
from chart.burndown import BurndownChart
import plotly.graph_objects as go


class DrawBurndownChartTask(Task):
    def __init__(self) -> None:
        self.jira_db = Database()
        self.burndown = BurndownChart()

    def run(self) -> None:
        sprint = self.jira_db.get_current_sprint()
        issues = self.jira_db.get_assigned_issues(sprint["id"])

        now = datetime.now().date()

        current_days = (now - sprint["start_date"]).days + 1

        total_points = sum(
            issue["story_points"] if issue["story_points"] else 0 for issue in issues
        )

        point_decrease = [0] * current_days

        for issue in issues:
            completion_date = issue["completion_date"]
            if completion_date:
                completion_day = (completion_date - sprint["start_date"]).days
                point_decrease[max(completion_day, 0)] -= issue["story_points"]

        day_points = []

        current_points = total_points

        for i in range(current_days):
            current_points += point_decrease[i]
            day_points.append(current_points)

        date_list = [
            sprint["start_date"] + timedelta(days=x)
            for x in range((now - sprint["start_date"]).days + 1)
        ]

        self.burndown.add_actual_chart(
            day_points,
            date_list,
        )
        self.burndown.add_ideal_chart(
            [total_points, 0],
            [sprint["start_date"], sprint["end_date"]],
        )
        title = f'{sprint["name"]} Burndown Chart'
        self.burndown.update_fig_layout(title)

        self.get_fig().show()

    def get_fig(self) -> go.Figure:
        return self.burndown.get_fig()
