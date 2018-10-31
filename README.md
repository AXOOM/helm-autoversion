# Kubernetes Helm Autoversion

Kubernetes Helm Autoversion is a small wrapper for [Kubernetes Helm](https://www.helm.sh/) that automatically downloads a Helm (client) version that matches the Tiller (server) version.

## Usage

First, ensure `0install` is in your `PATH`. If not, you can get it at http://0install.net/.

Next, run the following command to create a `helm` command-line alias for the wrapper:

    0alias helm http://assets.axoom.cloud/tools/helm-autoversion.xml

## Releasing

To package a new release of Kubernetes Helm Autoversion as a Zero Install feed run:

    0install run http://0install.net/tools/0template.xml helm-autoversion.xml.template version=0.1
