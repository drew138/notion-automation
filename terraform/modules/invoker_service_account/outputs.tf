output "service_account_email" {
  value       = google_service_account.scheduler-sa.email
  description = "Service account email used to invoke the Cloud Run job"
}
