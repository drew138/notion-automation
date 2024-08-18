resource "google_service_account" "scheduler-sa" {
  account_id   = "scheduler-sa"
  description  = "Cloud Scheduler service account"
  display_name = "scheduler-sa"

  lifecycle {
    prevent_destroy = true
  }
}
