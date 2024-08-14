module "append_transactions_database" {
  source = "./services/append_transactions_database"
}

module "draw_burndown_chart" {
  source = "./services/draw_burndown_chart"
}

module "draw_completion_chart" {
  source = "./services/draw_completion_chart"
}

module "draw_expenses_distribution_chart" {
  source = "./services/draw_expenses_distribution_chart"
}

module "draw_transactions_distributions_chart" {
  source = "./services/draw_transactions_distributions_chart"
}

module "update_assigned_issues_database" {
  source = "./services/update_assigned_issues_database"
}

module "update_reviewer_issues_database" {
  source = "./services/update_reviewer_issues_database"
}
