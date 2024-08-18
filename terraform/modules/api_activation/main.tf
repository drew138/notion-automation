resource "google_project_service" "cloudresourcemanager_api" {
  project = var.project_id
  service = "cloudresourcemanager.googleapis.com"
}

resource "google_project_service" "iam_api" {
  project    = var.project_id
  service    = "iam.googleapis.com"
  depends_on = [google_project_service.cloudresourcemanager_api]
}

resource "google_project_service" "run_api" {
  project    = var.project_id
  service    = "run.googleapis.com"
  depends_on = [google_project_service.cloudresourcemanager_api]
}

resource "google_project_service" "scheduler_api" {
  project    = var.project_id
  service    = "cloudscheduler.googleapis.com"
  depends_on = [google_project_service.cloudresourcemanager_api]
}

