#!/bin/bash
# deploy.sh: Automates deployment of SkyOptima using Docker and Kubernetes.

echo "Starting deployment of SkyOptima..."

# Build Docker image
docker build -t skyoptima:latest deploy/Dockerfile

# Push Docker image to registry (if applicable)
# docker push your-registry/skyoptima:latest

# Apply Kubernetes deployment
kubectl apply -f deploy/k8s_deployment.yaml

echo "Deployment initiated. Monitoring rollout status..."
kubectl rollout status deployment/skyoptima-deployment

echo "Deployment completed successfully."
