provider "google" {
  project = var.project_id
  region  = var.location
}

terraform {
  backend "gcs" {
    bucket = var.terraform_backend_gcs_bucket_name
    prefix = "terraform.tfstate"
  }
}
