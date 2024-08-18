variable "project_id" {
  type        = string
  description = "Google Cloud project id"
}

variable "location" {
  type        = string
  default     = "southamerica-east1"
  description = "Google cloud location"
}

variable "docker_image" {
  type        = string
  description = "Docker image to deploy in cloud run"
}

variable "notion_token" {
  type        = string
  description = "Notion token"
}

variable "notion_subscriptions_database_id" {
  type        = string
  description = "Notion subscriptions database id"
}

variable "notion_transactions_database_id" {
  type        = string
  description = "Notion transactions database id"
}

variable "notion_assigned_issues_database_id" {
  type        = string
  description = "Notion assigned issues database id"
}

variable "notion_reviewer_issues_database_id" {
  type        = string
  description = "Notion reviewer issues database id"
}

variable "jira_base_url" {
  type        = string
  description = "Jira base url"
}

variable "jira_access_token" {
  type        = string
  description = "Jira access token"
}

variable "jira_board_id" {
  type        = string
  description = "Jira board id"
}

variable "jira_project" {
  type        = string
  description = "Jira project"
}

variable "jira_story_points_custom_field" {
  type        = string
  description = "Jira story points custom field"
}

variable "jira_reviewer_custom_field" {
  type        = string
  description = "Jira reviewer custom field"
}
