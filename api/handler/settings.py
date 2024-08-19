from typing import Dict, Tuple, Callable
from api.handler.work import (
    draw_burndown_chart,
    draw_completion_chart,
    update_assigned_issues_database,
    update_reviewever_issues_database,
)
from api.handler.finances import (
    draw_expenses_distribution_chart,
    draw_transactions_distribution_chart,
    append_transactions_database,
)

handler_config: Dict[str, Tuple[str, Callable]] = {
    "draw_expenses_distribution_chart": (
        "GET",
        draw_expenses_distribution_chart.index,
    ),
    "draw_transactions_distribution_chart": (
        "GET",
        draw_transactions_distribution_chart.index,
    ),
    "draw_burndown_chart": (
        "GET",
        draw_burndown_chart.index,
    ),
    "draw_completion_chart": (
        "GET",
        draw_completion_chart.index,
    ),
    "append_transactions_database": (
        "POST",
        append_transactions_database.index,
    ),
    "update_assigned_issues_database": (
        "POST",
        update_assigned_issues_database.index,
    ),
    "update_reviewer_issues_database": (
        "POST",
        update_reviewever_issues_database.index,
    ),
}
