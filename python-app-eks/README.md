# Python App EKS Template

Backstage software template for creating Python Flask applications deployed to Amazon EKS via ArgoCD.

## Features

- 🐍 **Python Flask Application** - Pre-configured Flask app with health/ready endpoints
- 📦 **Docker Container** - Multi-stage Dockerfile optimized for production
- ⎈ **Helm Chart** - Kubernetes deployment with configurable values
- 🔄 **ArgoCD GitOps** - Automated deployment via ArgoCD
- 📚 **TechDocs** - MkDocs documentation ready for Backstage
- 🚀 **CI/CD Workflows** - GitHub Actions for build and deploy

## Prerequisites

Before creating an application, ensure the `ghcr-secret` exists in your target namespace (or default) to allow pulling images from GitHub Container Registry.

```bash
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=<GITHUB_USER> \
  --docker-password=<GITHUB_PAT>
```

## Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `name` | ✅ | - | Application name (kebab-case) |
| `description` | ✅ | - | Brief description |
| `owner` | ✅ | - | Team ownership |
| `python_version` | ✅ | 3.11 | Python runtime version |
| `container_port` | ❌ | 8080 | Container port |
| `namespace` | ✅ | default | Kubernetes namespace |
| `replicas` | ❌ | 1 | Pod replicas |

## Generated Structure

```
{app-name}/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── charts/{app-name}/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── docs/
│   ├── index.md
│   ├── deployment.md
│   └── api.md
├── .github/workflows/
│   ├── build.yml
│   └── deploy.yml
├── mkdocs.yml
├── catalog-info.yaml
└── README.md
```

## Usage

1. Open Backstage Portal
2. Navigate to **Create** → **Choose a template**
3. Select **Python App on EKS**
4. Fill in the parameters
5. Click **Create**

After creation:
1. Push to trigger the build workflow
2. Run the **Deploy to EKS** workflow
3. View your app in ArgoCD
