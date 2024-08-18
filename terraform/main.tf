module "api_activation" {
  source     = "./modules/api_activation"
  project_id = var.project_id
}

module "invoker_service_account" {
  source     = "./modules/invoker_service_account"
  depends_on = [module.api_activation]
}

module "append_transactions_database" {
  source                = "./modules/scheduled_task"
  service_name          = "append-transactions-database"
  docker_image          = var.docker_image
  location              = var.location
  service_account_email = module.invoker_service_account.service_account_email
  environment_variables = [
    {
      name  = "ROUTE"
      value = "append_transactions_database"
    },
    {
      name  = "NOTION_TOKEN"
      value = var.notion_token
    },
    {
      name  = "NOTION_SUBSCRIPTIONS_DATABASE_ID"
      value = var.notion_subscriptions_database_id
    },
    {
      name  = "NOTION_TRANSACTIONS_DATABASE_ID"
      value = var.notion_transactions_database_id
    },
  ]
}

module "update_assigned_issues_database" {
  source                = "./modules/scheduled_task"
  service_name          = "update-assigned-issues-database"
  docker_image          = var.docker_image
  location              = var.location
  service_account_email = module.invoker_service_account.service_account_email
  environment_variables = [
    {
      name  = "ROUTE"
      value = "update_assigned_issues_database"
    },
    {
      name  = "JIRA_BASE_URL"
      value = var.jira_base_url
    },
    {
      name  = "JIRA_ACCESS_TOKEN"
      value = var.jira_access_token
    },
    {
      name  = "JIRA_BOARD_ID"
      value = var.jira_board_id
    },
    {
      name  = "JIRA_PROJECT"
      value = var.jira_project
    },
    {
      name  = "JIRA_STORY_POINTS_CUSTOM_FIELD"
      value = var.jira_story_points_custom_field
    },
    {
      name  = "JIRA_REVIEWER_CUSTOM_FIELD"
      value = var.jira_reviewer_custom_field
    },
    {
      name  = "NOTION_TOKEN"
      value = var.notion_token
    },
    {
      name  = "NOTION_ASSIGNED_ISSUES_DATABASE_ID"
      value = var.notion_assigned_issues_database_id
    },
  ]
}

module "update_reviewer_issues_database" {
  source                = "./modules/scheduled_task"
  service_name          = "update-reviewer-issues-database"
  docker_image          = var.docker_image
  location              = var.location
  service_account_email = module.invoker_service_account.service_account_email
  environment_variables = [
    {
      name  = "ROUTE"
      value = "update_reviewer_issues_database"
    },
    {
      name  = "JIRA_BASE_URL"
      value = var.jira_base_url
    },
    {
      name  = "JIRA_ACCESS_TOKEN"
      value = var.jira_access_token
    },
    {
      name  = "JIRA_BOARD_ID"
      value = var.jira_board_id
    },
    {
      name  = "JIRA_PROJECT"
      value = var.jira_project
    },
    {
      name  = "JIRA_STORY_POINTS_CUSTOM_FIELD"
      value = var.jira_story_points_custom_field
    },
    {
      name  = "JIRA_REVIEWER_CUSTOM_FIELD"
      value = var.jira_reviewer_custom_field
    },
    {
      name  = "NOTION_TOKEN"
      value = var.notion_token
    },
    {
      name  = "NOTION_REVIEWER_ISSUES_DATABASE_ID"
      value = var.notion_reviewer_issues_database_id
    },
  ]
}

module "draw_burndown_chart" {
  source       = "./modules/task"
  service_name = "draw-burndown-chart"
  docker_image = var.docker_image
  location     = var.location
  environment_variables = [
    {
      name  = "ROUTE"
      value = "draw_burndown_chart"
    },
    {
      name  = "JIRA_BASE_URL"
      value = var.jira_base_url
    },
    {
      name  = "JIRA_ACCESS_TOKEN"
      value = var.jira_access_token
    },
    {
      name  = "JIRA_BOARD_ID"
      value = var.jira_board_id
    },
    {
      name  = "JIRA_PROJECT"
      value = var.jira_project
    },
    {
      name  = "JIRA_STORY_POINTS_CUSTOM_FIELD"
      value = var.jira_story_points_custom_field
    },
    {
      name  = "JIRA_REVIEWER_CUSTOM_FIELD"
      value = var.jira_reviewer_custom_field
    },
  ]
}

module "draw_completion_chart" {
  source       = "./modules/task"
  service_name = "draw-completion-chart"
  docker_image = var.docker_image
  location     = var.location
  environment_variables = [
    {
      name  = "ROUTE"
      value = "draw_completion_chart"
    },
    {
      name  = "JIRA_BASE_URL"
      value = var.jira_base_url
    },
    {
      name  = "JIRA_ACCESS_TOKEN"
      value = var.jira_access_token
    },
    {
      name  = "JIRA_BOARD_ID"
      value = var.jira_board_id
    },
    {
      name  = "JIRA_PROJECT"
      value = var.jira_project
    },
    {
      name  = "JIRA_STORY_POINTS_CUSTOM_FIELD"
      value = var.jira_story_points_custom_field
    },
    {
      name  = "JIRA_REVIEWER_CUSTOM_FIELD"
      value = var.jira_reviewer_custom_field
    },
  ]
}

module "draw_expenses_distribution_chart" {
  source       = "./modules/task"
  service_name = "draw-expenses-distribution-chart"
  docker_image = var.docker_image
  location     = var.location
  environment_variables = [
    {
      name  = "ROUTE"
      value = "draw_expenses_distribution_chart"
    },
    {
      name  = "NOTION_TOKEN"
      value = var.notion_token
    },
    {
      name  = "NOTION_TRANSACTIONS_DATABASE_ID"
      value = var.notion_transactions_database_id
    },
  ]
}

module "draw_transactions_distributions_chart" {
  source       = "./modules/task"
  service_name = "draw-transactions-distributions-chart"
  docker_image = var.docker_image
  location     = var.location
  environment_variables = [
    {
      name  = "ROUTE"
      value = "draw_transactions_distribution_chart"
    },
    {
      name  = "NOTION_TOKEN"
      value = var.notion_token
    },
    {
      name  = "NOTION_TRANSACTIONS_DATABASE_ID"
      value = var.notion_transactions_database_id
    },
  ]
}

