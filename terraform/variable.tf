variable "location" {
  type        = string
  default     = "southamerica-east1"
  description = "Google cloud location"
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

variable "docker_image" {
  type        = string
  description = "Docker image to deploy in Cloud Run"
}
