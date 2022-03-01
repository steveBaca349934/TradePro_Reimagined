## Build Image Locally

* docker build -t registry.digitalocean.com/tradepro-reimagined-k8s/tradepro-reimagined-web:latest -f Dockerfile .

## Push to Digital Ocean Container Repo

* docker push registry.digitalocean.com/tradepro-reimagined-k8s/tradepro-reimagined-web --all-tags