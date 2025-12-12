# Deployment Guide

## Prerequisites

- Access to the EKS cluster
- ArgoCD access
- AWS credentials configured

## Deployment Architecture

This application uses GitOps principles with ArgoCD:

1. **GitHub Repository**: Source of truth for application code and Kubernetes manifests
2. **GitHub Actions**: Builds Docker images and pushes to ECR
3. **ArgoCD**: Watches the repository and deploys changes to EKS
4. **Amazon ECR**: Container registry storing Docker images
5. **Amazon EKS**: Kubernetes cluster running the application

## Initial Deployment

The first deployment is triggered via GitHub Actions:

1. Go to **Actions** → **Deploy to EKS**
2. Click **Run workflow**
3. Select the branch (usually `main`)
4. Click **Run workflow**

This will:
- Register the repository in ArgoCD
- Create the ArgoCD Application
- Deploy to EKS

## Viewing Deployment Status

### ArgoCD UI

Access the ArgoCD dashboard at `https://argocd.demotw.com` and navigate to your application.

### Kubernetes

```bash
# Get pods
kubectl get pods -n ${{ values.namespace }}

# Get service
kubectl get svc -n ${{ values.namespace }}

# View logs
kubectl logs -n ${{ values.namespace }} -l app.kubernetes.io/name=${{ values.name }}
```

## Accessing the Application

### Internal Access (Port Forward)

```bash
kubectl port-forward -n ${{ values.namespace }} svc/${{ values.name }} 8080:80
curl http://localhost:8080
```

### Service DNS

Within the cluster, the service is accessible at:
```
${{ values.name }}.${{ values.namespace }}.svc.cluster.local
```

## Helm Configuration

The Helm chart is located at `charts/${{ values.name }}/`.

### Key Values

| Parameter | Default | Description |
|-----------|---------|-------------|
| `replicaCount` | ${{ values.replicas }} | Number of pod replicas |
| `image.repository` | ECR repo | Container image repository |
| `image.tag` | latest | Image tag |
| `service.port` | 80 | Service port |
| `service.targetPort` | ${{ values.container_port }} | Container port |

## Troubleshooting

### Pod not starting

```bash
# Check pod events
kubectl describe pod -n ${{ values.namespace }} -l app.kubernetes.io/name=${{ values.name }}

# Check logs
kubectl logs -n ${{ values.namespace }} -l app.kubernetes.io/name=${{ values.name }}
```

### ArgoCD sync issues

1. Check ArgoCD application status
2. Verify Helm chart validity: `helm template charts/${{ values.name }}`
3. Check repository access in ArgoCD
