data "google_artifact_registry_docker_image" "default" {
  location      = var.location
  repository_id = var.repository_id
  image_name    = "my-image:my-tag"
}
