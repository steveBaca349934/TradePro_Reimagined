## Command to create secrets

* kubectl create secret generic tradepro-reimagined-web-prod-env --from-env-file=TradePro_Reimagined/.env.prod

## Command to deploy app to k8s

* kubectl apply -f k8s/apps/tradepro-reimagined-web.yaml

## Command to restart deployment 

* kubectl rollout restart deployment/tradepro-reimagined-web-deployment