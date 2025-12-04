# 🛠️ Backstage Templates

Software scaffolding templates for Backstage Beach portal.

## Overview

This repository contains Backstage Software Templates for creating new projects with AWS best practices and standardized configurations.

## Available Templates

### Coming Soon

- **Python Lambda Function** - Serverless function with CI/CD
- **Python Flask API** - REST API on ECS/Fargate
- **Static Website** - S3 + CloudFront deployment
- **Terraform Module** - Reusable infrastructure components
- **Docker Container** - Containerized application with ECR

## Template Structure

Each template includes:

```
template-name/
├── template.yaml          # Backstage template definition
├── skeleton/             # Project template files
│   ├── src/
│   ├── tests/
│   ├── .github/
│   │   └── workflows/
│   ├── README.md
│   └── catalog-info.yaml
└── docs/
    └── index.md
```

## Using Templates

1. Access Backstage Beach portal
2. Navigate to **Create** → **Choose a template**
3. Fill in project details
4. Template generates repository with:
   - Source code structure
   - CI/CD pipeline
   - Documentation
   - Backstage catalog metadata

## Creating New Templates

See [Template Development Guide](./docs/TEMPLATE_DEVELOPMENT.md)

## Contributing

See [CONTRIBUTING.md](https://github.com/backstage-beach/.github/blob/main/CONTRIBUTING.md)

## License

Apache 2.0
