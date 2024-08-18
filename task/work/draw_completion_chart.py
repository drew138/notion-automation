from task.task import Task
from jira.database.database import Database
from chart.pie import PieChart
import plotly.graph_objects as go
from collections import defaultdict


class DrawCompletionChartTask(Task):
    def __init__(self) -> None:
        self.jira_db = Database()
        self.pie = PieChart()

    def run(self) -> None:
        sprint = self.jira_db.get_current_sprint()
        issues = self.jira_db.get_assigned_issues(sprint["id"])

        counts = defaultdict(int)

        for issue in issues:
            if issue["story_points"]:
                counts[issue["status"]] += issue["story_points"]

        self.pie.add_chart(list(counts.keys()), list(counts.values()))

        self.pie.update_fig_layout("Issue Completion Distribution")

        self.get_fig().show()

    def get_fig(self) -> go.Figure:
        return self.pie.get_fig()
