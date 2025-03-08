provider "google" {
  project = "votre-projet"
  region  = "us-central1"
}

resource "google_container_cluster" "primary" {
  name     = "flask-app-cluster"
  location = "us-central1"

  initial_node_count = 3

  node_config {
    machine_type = "e2-medium"
  }
}