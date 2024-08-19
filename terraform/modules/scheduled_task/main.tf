resource "random_id" "id" {
  keepers = {
    first = "${timestamp()}"
  }
  byte_length = 8
}

resource "google_cloud_run_v2_service" "job" {
  name     = format("%s-job", var.service_name)
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    revision = format("%s-job-%s", var.service_name, random_id.id.hex)

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

  traffic {
    percent  = 100
    revision = format("%s-job-%s", var.service_name, random_id.id.hex)
  }
}

resource "google_cloud_run_service_iam_member" "job_iam_member" {
  location = var.location
  service  = google_cloud_run_v2_service.job.name
  role     = "roles/run.invoker"
  member   = "serviceAccount:${var.service_account_email}"
}


resource "google_cloud_scheduler_job" "trigger" {
  name             = format("%s-trigger", var.service_name)
  region           = var.location
  description      = "Invoke a Cloud Run container on an hourly basis."
  schedule         = "0 * * * *"
  time_zone        = var.timezone
  attempt_deadline = "300s"

  retry_config {
    retry_count = 1
  }

  http_target {
    http_method = "POST"
    uri         = google_cloud_run_v2_service.job.uri

    oidc_token {
      service_account_email = var.service_account_email
    }
  }
}
