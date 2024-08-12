variable "location" {
  type        = string
  default     = "southamerica-east1"
  description = "Google cloud location"
}

variable "repository_id" {
  type        = string
  default     = "notion_automations"
  description = "Google Artifact Registry repository id"
}

variable "timezone" {
  type        = string
  default     = "America/Bogota"
  description = "Timezone for cloud scheduler jobs"
}

variable "project_id" {
  type        = string
  description = "Google Cloud project id"
}
