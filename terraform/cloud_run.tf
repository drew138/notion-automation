resource "google_cloud_run_v2_service" "update_assigned_issues_database_job" {
  name     = "update-assigned-issues-database-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.my_image.self_link
      env {
        name  = "ROUTE"
        value = "update_assigned_issues_database"
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

resource "google_cloud_run_v2_service" "update_reviewer_issues_database_job" {
  name     = "update-reviewer-issues-database-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.my_image.self_link
      env {
        name  = "ROUTE"
        value = "update_reviewer_issues_database"
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

resource "google_cloud_run_v2_service" "append_transactions_database_job" {
  name     = "append-transactions-database-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.default.self_link
      env {
        name  = "ROUTE"
        value = "append_transactions_database"
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

resource "google_cloud_run_v2_service" "draw_burndown_chart_job" {
  name     = "draw-burndown-chart-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.default.self_link
      env {
        name  = "ROUTE"
        value = "draw_burndown_chart"
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

resource "google_cloud_run_v2_service" "draw_completion_chart_job" {
  name     = "draw-completion-chart-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.default.self_link
      env {
        name  = "ROUTE"
        value = "draw_completion_chart"
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

resource "google_cloud_run_v2_service" "draw_expenses_distribution_chart_job" {
  name     = "draw-expenses-distribution-chart-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.default.self_link
      env {
        name  = "ROUTE"
        value = "draw_expenses_distribution_chart"
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

resource "google_cloud_run_v2_service" "draw_transactions_distribution_chart_job" {
  name     = "draw-transactions-distribution-chart-job"
  location = var.location

  template {

    scaling {
      max_instance_count = 1
      min_instance_count = 0
    }

    containers {
      image = data.google_artifact_registry_docker_image.default.self_link
      env {
        name  = "ROUTE"
        value = "draw_transactions_distribution_chart"
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
