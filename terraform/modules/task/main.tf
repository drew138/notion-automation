resource "google_cloud_run_v2_service" "job" {
  name     = format("%s-job", var.service_name)
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = var.docker_image

      ports {
        container_port = 3000
      }

      dynamic "env" {
        for_each = var.environment_variables
        content {
          name  = env.value["name"]
          value = env.value["value"]
        }
      }
    }
  }
}

resource "google_cloud_run_service_iam_member" "job_iam_member" {
  location = var.location
  service  = google_cloud_run_v2_service.job.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
