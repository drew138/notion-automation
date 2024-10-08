variable "service_name" {
  type        = string
  description = "Name of the Cloud Run job"
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

variable "environment_variables" {
  description = "List of environment variables"
  type = list(object({
    name  = string
    value = string
  }))
  default = []
}
