resource "google_cloud_run_v2_service" "draw_burndown_chart_job" {
  name     = "draw-burndown-chart-job"
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
        value = "draw_burndown_chart"
      }
      env {
        name  = "JIRA_BASE_URL"
        value = env("JIRA_BASE_URL")
      }
      env {
        name  = "JIRA_ACCESS_TOKEN"
        value = env("JIRA_ACCESS_TOKEN")
      }
      env {
        name  = "JIRA_BOARD_ID"
        value = env("JIRA_BOARD_ID")
      }
      env {
        name  = "JIRA_PROJECT"
        value = env("JIRA_PROJECT")
      }
      env {
        name  = "JIRA_STORY_POINTS_CUSTOM_FIELD"
        value = env("JIRA_STORY_POINTS_CUSTOM_FIELD")
      }
      env {
        name  = "JIRA_REVIEWER_CUSTOM_FIELD"
        value = env("JIRA_REVIEWER_CUSTOM_FIELD")
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

resource "google_cloud_run_service_iam_member" "draw_burndown_chart_job_member" {
  location = var.location
  service  = google_cloud_run_v2_service.draw_burndown_chart_job.name
  role     = "roles/run.invoker"
  member   = "allUsers"

  depends_on = [
    google_project_service.iam_api,
  ]
}
