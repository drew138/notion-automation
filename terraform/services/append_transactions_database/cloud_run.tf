resource "google_cloud_run_v2_service" "append_transactions_database_job" {
  name     = "append-transactions-database-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = var.docker_image
      env {
        name  = "ROUTE"
        value = "append_transactions_database"
      }
      env {
        name  = "NOTION_TOKEN"
        value = env("NOTION_TOKEN")
      }
      env {
        name  = "NOTION_SUBSCRIPTIONS_DATABASE_ID"
        value = env("NOTION_SUBSCRIPTIONS_DATABASE_ID")
      }
      env {
        name  = "NOTION_TRANSACTIONS_DATABASE_ID"
        value = env("NOTION_TRANSACTIONS_DATABASE_ID")
      }
    }
  }

  traffic {
    percent = 100
  }

  depends_on = [
    google_project_service.run_api,
  ]
}

resource "google_cloud_run_service_iam_member" "append_transactions_database_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.append_transactions_database_job.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${google_service_account.scheduler-sa.email}"

  depends_on = [
    google_project_service.iam_api,
  ]
}
