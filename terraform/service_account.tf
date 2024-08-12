resource "google_service_account" "scheduler-sa" {
  account_id   = "scheduler-sa"
  description  = "Cloud Scheduler service account"
  display_name = "scheduler-sa"

  depends_on = [
    google_project_service.iam_api
  ]
}

# Authenticated invoker
resource "google_cloud_run_service_iam_member" "update_assigned_issues_database_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.update_assigned_issues_database_job.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.scheduler-sa.email}"
}

resource "google_cloud_run_service_iam_member" "update_reviewer_issues_database_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.update_reviewer_issues_database_job.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.scheduler-sa.email}"
}

resource "google_cloud_run_service_iam_member" "append_transactions_database_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.append_transactions_database_job.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.scheduler-sa.email}"
}

# Unauthenticated invoker
resource "google_cloud_run_service_iam_member" "draw_expenses_distribution_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_expenses_distribution_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_cloud_run_service_iam_member" "draw_transactions_distribution_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_transactions_distribution_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_cloud_run_service_iam_member" "draw_burndown_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_burndown_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}

resource "google_cloud_run_service_iam_member" "draw_completion_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_completion_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
