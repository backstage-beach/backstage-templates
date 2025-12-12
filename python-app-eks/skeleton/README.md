# ${{ values.name }}

${{ values.description }}

## 🚀 Quick Start

### Prerequisites

- Python ${{ values.python_version }}+
- Docker
- AWS CLI configured
- Access to EKS cluster

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt

# Run locally
cd app && python app.py
```

Visit http://localhost:${{ values.container_port }}

### Deploy to EKS

1. Push changes to `main` branch to build the Docker image
2. Go to **Actions** → **Deploy to EKS** → **Run workflow**

## 📁 Project Structure

```
.
├── app/                    # Application code
│   ├── app.py             # Flask application
│   ├── Dockerfile         # Container build
│   └── requirements.txt   # Python dependencies
├── charts/                 # Helm charts
│   └── ${{ values.name }}/
├── docs/                   # Documentation (TechDocs)
├── .github/workflows/      # CI/CD pipelines
└── catalog-info.yaml       # Backstage catalog entry
```

## 📖 Documentation

Full documentation is available in Backstage TechDocs.

## 🔗 Links

- [ArgoCD Application](https://argocd.demotw.com/applications/${{ values.name }})
- [Backstage Catalog](https://backstage.demotw.com/catalog/default/component/${{ values.name }})

## 👥 Owner

${{ values.owner }}
