resource "google_cloud_run_v2_service" "draw_expenses_distribution_chart_job" {
  name     = "draw-expenses-distribution-chart-job"
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
        value = "draw_expenses_distribution_chart"
      }
      env {
        name = "NOTION_TOKEN"
        value = env("NOTION_TOKEN")
      }
      env {
        name = "NOTION_TRANSACTIONS_DATABASE_ID"
        value = env("NOTION_TRANSACTIONS_DATABASE_ID")
      }
    }
  }

  traffic {
    percent = 100
  }

  depends_on = [
    google_project_service.run_api
  ]
}

resource "google_cloud_run_service_iam_member" "draw_expenses_distribution_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_expenses_distribution_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
