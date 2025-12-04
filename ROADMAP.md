# Backstage Templates - Development Roadmap

## 📋 Overview

This document outlines the development strategy for creating software templates for Backstage Beach portal.

## 🎯 Objectives

1. Provide production-ready software templates
2. Follow AWS and Backstage best practices
3. Include complete CI/CD pipelines
4. Ensure templates are self-documenting
5. Support multiple programming languages

## 📅 Development Phases

### Phase 1: Foundation & Infrastructure (Week 1)

#### Repository Setup
- [x] Initialize repository structure
- [ ] Create template development guidelines
- [ ] Setup template testing framework
- [ ] Configure pre-commit hooks
- [ ] Create GitHub Actions for template validation

#### Documentation
- [ ] Template development guide
- [ ] Template user guide
- [ ] Best practices documentation
- [ ] Troubleshooting guide

#### Template Structure Standard
```
template-name/
├── template.yaml              # Backstage template definition
├── skeleton/                  # Template source code
│   ├── .github/
│   │   └── workflows/
│   │       ├── ci.yml
│   │       └── deploy.yml
│   ├── src/
│   ├── tests/
│   ├── docs/
│   ├── README.md
│   ├── .gitignore
│   ├── catalog-info.yaml
│   └── [language-specific files]
├── docs/
│   ├── index.md
│   └── usage.md
└── README.md
```

### Phase 2: Serverless Templates (Weeks 2-3)

#### Python Lambda Function Template
**Priority: HIGH**

```
python-lambda-function/
├── template.yaml
├── skeleton/
│   ├── src/
│   │   ├── lambda_function.py
│   │   ├── requirements.txt
│   │   └── utils/
│   ├── tests/
│   │   ├── test_lambda.py
│   │   └── conftest.py
│   ├── .github/workflows/
│   │   ├── ci.yml          # Test and lint
│   │   └── deploy.yml      # Deploy to AWS
│   ├── terraform/          # Infrastructure as Code
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── catalog-info.yaml
│   └── README.md
```

**Tasks:**
- [ ] Create template.yaml with parameters:
  - Function name
  - Runtime (Python 3.9, 3.10, 3.11, 3.12)
  - Memory size
  - Timeout
  - Environment variables
  - IAM role permissions
- [ ] Implement skeleton with:
  - Sample Lambda handler
  - Unit tests with pytest
  - Integration tests
  - Requirements management
  - Environment-specific configs
- [ ] Add CI/CD pipeline:
  - Linting (pylint, black, mypy)
  - Security scanning (bandit)
  - Unit tests
  - Deploy to dev/staging/prod
- [ ] Create Terraform module:
  - Lambda function
  - CloudWatch Log Group
  - IAM role with least privilege
  - API Gateway (optional)
  - EventBridge trigger (optional)
- [ ] Documentation:
  - Setup instructions
  - Local development guide
  - Deployment guide
  - Monitoring and logging

#### Node.js Lambda Function Template
**Priority: MEDIUM**

Similar structure to Python Lambda, adapted for Node.js:
- Use npm/yarn for dependencies
- Jest for testing
- ESLint for linting
- Support TypeScript option

### Phase 3: Container Templates (Week 4)

#### Python Flask API on ECS/Fargate
```
python-flask-ecs/
├── template.yaml
├── skeleton/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── config.py
│   ├── tests/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── .github/workflows/
│   │   ├── ci.yml
│   │   └── deploy.yml
│   ├── terraform/
│   │   ├── ecs.tf
│   │   ├── alb.tf
│   │   ├── ecr.tf
│   │   └── vpc.tf
│   └── catalog-info.yaml
```

**Tasks:**
- [ ] Flask application skeleton
- [ ] Docker multi-stage build
- [ ] ECS task definition
- [ ] Fargate service configuration
- [ ] ALB setup with health checks
- [ ] Auto-scaling policies
- [ ] CloudWatch dashboards
- [ ] CI/CD with ECR and ECS deployment

#### FastAPI Microservice Template
**Priority: MEDIUM**

- Modern async Python framework
- OpenAPI/Swagger auto-generation
- Pydantic data validation
- Docker deployment ready

### Phase 4: Static & Frontend Templates (Week 5)

#### Static Website (S3 + CloudFront)
```
static-website-s3/
├── template.yaml
├── skeleton/
│   ├── public/
│   │   ├── index.html
│   │   ├── css/
│   │   ├── js/
│   │   └── assets/
│   ├── terraform/
│   │   ├── s3.tf
│   │   ├── cloudfront.tf
│   │   ├── route53.tf       # Optional
│   │   └── acm.tf           # Optional
│   ├── .github/workflows/
│   │   └── deploy.yml
│   └── catalog-info.yaml
```

**Tasks:**
- [ ] Static HTML skeleton
- [ ] S3 bucket with website hosting
- [ ] CloudFront distribution
- [ ] Optional custom domain setup
- [ ] Cache invalidation in CI/CD
- [ ] Security headers
- [ ] Cost optimization

#### React SPA Template
**Priority: MEDIUM**

- Create React App or Vite
- TypeScript support
- S3 + CloudFront deployment
- Environment-specific configs

### Phase 5: Infrastructure Templates (Week 6)

#### Terraform Module Template
```
terraform-module/
├── template.yaml
├── skeleton/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── versions.tf
│   ├── examples/
│   │   └── basic/
│   ├── tests/
│   │   └── terraform_test.go
│   ├── .github/workflows/
│   │   ├── validate.yml
│   │   └── release.yml
│   ├── README.md
│   └── catalog-info.yaml
```

**Tasks:**
- [ ] Terraform module structure
- [ ] Input validation
- [ ] Output documentation
- [ ] Usage examples
- [ ] Terratest integration
- [ ] terraform-docs automation
- [ ] Semantic versioning
- [ ] GitHub release workflow

#### CloudFormation Stack Template
**Priority: LOW**

- YAML/JSON templates
- Parameter validation
- Stack policies
- Change sets

### Phase 6: Data & Analytics Templates (Week 7)

#### Python ETL Job (Glue/EMR)
- [ ] AWS Glue job template
- [ ] PySpark transformations
- [ ] Data catalog integration
- [ ] Schedule configuration

#### Data Pipeline Template
- [ ] Step Functions orchestration
- [ ] Lambda data processing
- [ ] S3 to Redshift pipeline
- [ ] Error handling and retry logic

### Phase 7: Specialized Templates (Week 8)

#### Machine Learning Model API
- [ ] SageMaker endpoint
- [ ] Model serving with Flask/FastAPI
- [ ] A/B testing support
- [ ] Model monitoring

#### Event-Driven Architecture
- [ ] EventBridge + Lambda
- [ ] SQS queue processing
- [ ] DLQ handling
- [ ] Message routing

## 🛠️ Template Development Standards

### template.yaml Structure
```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: python-lambda-function
  title: Python Lambda Function
  description: Create a serverless Python Lambda function with CI/CD
  tags:
    - aws
    - lambda
    - python
    - serverless
spec:
  owner: platform-team
  type: service
  
  parameters:
    - title: Project Information
      required:
        - name
        - description
      properties:
        name:
          title: Function Name
          type: string
          description: Name of the Lambda function
          pattern: '^[a-z0-9-]+$'
        description:
          title: Description
          type: string
          description: Brief description of the function
        owner:
          title: Owner
          type: string
          description: Team or person responsible
          ui:field: OwnerPicker
          ui:options:
            catalogFilter:
              kind: Group
              
    - title: AWS Configuration
      required:
        - runtime
        - memory
      properties:
        runtime:
          title: Python Runtime
          type: string
          enum:
            - python3.9
            - python3.10
            - python3.11
            - python3.12
          default: python3.11
        memory:
          title: Memory (MB)
          type: number
          enum: [128, 256, 512, 1024, 2048, 3008]
          default: 512
        timeout:
          title: Timeout (seconds)
          type: number
          default: 30
          minimum: 3
          maximum: 900
        
    - title: Repository Configuration
      required:
        - repoUrl
      properties:
        repoUrl:
          title: Repository Location
          type: string
          ui:field: RepoUrlPicker
          ui:options:
            allowedHosts:
              - github.com
            allowedOwners:
              - backstage-beach
              
  steps:
    - id: fetch
      name: Fetch Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          description: ${{ parameters.description }}
          owner: ${{ parameters.owner }}
          runtime: ${{ parameters.runtime }}
          memory: ${{ parameters.memory }}
          timeout: ${{ parameters.timeout }}
          
    - id: publish
      name: Publish to GitHub
      action: publish:github
      input:
        allowedHosts: ['github.com']
        description: ${{ parameters.description }}
        repoUrl: ${{ parameters.repoUrl }}
        defaultBranch: main
        repoVisibility: public
        
    - id: register
      name: Register Component
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps.publish.output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'
        
  output:
    links:
      - title: Repository
        url: ${{ steps.publish.output.remoteUrl }}
      - title: Open in Backstage
        icon: catalog
        entityRef: ${{ steps.register.output.entityRef }}
```

### Skeleton Best Practices

1. **Parameterization**: Use `${{ values.parameter }}` placeholders
2. **Documentation**: README.md with setup instructions
3. **Tests**: Include sample tests
4. **CI/CD**: Complete pipeline ready to use
5. **IaC**: Infrastructure code included
6. **Security**: Secrets management, IAM least privilege
7. **Monitoring**: CloudWatch dashboards and alarms
8. **Cost**: Cost estimation and optimization notes

### Testing Templates

Create test script:
```bash
#!/bin/bash
# test-template.sh

TEMPLATE_NAME=$1

# Validate template.yaml
backstage-cli template:validate $TEMPLATE_NAME/template.yaml

# Test parameter combinations
backstage-cli template:test $TEMPLATE_NAME \
  --parameters '{"name":"test-function","runtime":"python3.11"}'

# Check skeleton files
find $TEMPLATE_NAME/skeleton -type f | while read file; do
  echo "Checking $file..."
  # Lint, validate, etc.
done
```

## 🔍 Quality Checklist

Before publishing template:
- [ ] template.yaml validates
- [ ] All parameters have descriptions
- [ ] Skeleton generates successfully
- [ ] CI/CD pipeline works
- [ ] Infrastructure deploys correctly
- [ ] Documentation complete
- [ ] Tests included and passing
- [ ] Security best practices followed
- [ ] Cost implications documented
- [ ] Example usage provided

## 🚀 Template Usage Flow

1. User opens Backstage Portal
2. Navigates to **Create** → **Choose a template**
3. Selects desired template
4. Fills in parameters
5. Template generates repository
6. CI/CD pipeline auto-triggered
7. Application deployed to AWS
8. Component registered in catalog

## 📚 Resources

- [Backstage Software Templates](https://backstage.io/docs/features/software-templates/)
- [Template Actions](https://backstage.io/docs/features/software-templates/builtin-actions)
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)

## 🤝 Contributing

See [CONTRIBUTING.md](https://github.com/backstage-beach/.github/blob/main/CONTRIBUTING.md)
