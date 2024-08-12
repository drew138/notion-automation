resource "google_artifact_registry_repository" "notion_automations" {
  location      = var.location
  repository_id = var.repository_id
  format        = "DOCKER"
}
