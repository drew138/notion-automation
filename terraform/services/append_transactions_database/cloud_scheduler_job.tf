resource "google_cloud_scheduler_job" "append_transactions_database_trigger" {
  name             = "append-transactions-database-trigger"
  region           = var.location
  description      = "Invoke a Cloud Run container on a schedule for appending subscription transactions in notion."
  schedule         = "0 * * * *"
  time_zone        = var.timezone
  attempt_deadline = "300s"

  retry_config {
    retry_count = 1
  }

  http_target {
    http_method = "POST"
    uri         = google_cloud_run_v2_service.default.uri

    oidc_token {
      service_account_email = google_service_account.scheduler-sa.email
    }
  }

  depends_on = [
    google_project_service.scheduler_api
  ]
}
