# Kubernetes Helm Autoversion

Kubernetes Helm Autoversion is a small wrapper for [Kubernetes Helm](https://www.helm.sh/) that automatically downloads a Helm (client) version that matches the Tiller (server) version.

## Usage

First, ensure `0install` is in your `PATH`. You can get it at http://0install.net/.

Next, run the following command to create a `helm` command-line alias for the wrapper:

    0install add helm http://repo.roscidus.com/kubernetes/helm-autoversion
