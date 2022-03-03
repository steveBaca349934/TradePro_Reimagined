1. Test Django
'''
python3 manage.py test
'''

2. Build Container
'''
docker build -f Dockerfile \
    -t registry.digitalocean.com/tradepro-reimagined-k8s/tradepro-reimagined-web:latest \
    -t registry.digitalocean.com/tradepro-reimagined-k8s/tradepro-reimagined-web:v1 \
    .
'''

3. Push Container to DO Repo
'''
docker push registry.digitalocean.com/tradepro-reimagined-k8s/tradepro-reimagined-web --all-tags
'''

4. Update Secrets
'''
kubectl delete secret generic tradepro-reimagined-web-prod-env
kubectl create secret generic tradepro-reimagined-web-prod-env --from-env-file=TradePro_Reimagined/.env.prod
'''

5. Update Deployment
'''
kubectl apply -f TradePro_Reimagined/k8s/apps/tradepro-reimagined-web.yaml

'''

6. Wait for Rollout to Finish
'''
kubectl rollout status deployment/tradepro-reimagined-web-deployment
'''

7. Migrate Database
'''

'''