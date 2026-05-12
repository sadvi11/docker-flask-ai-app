# Docker Flask AI App

> Flask AI Spam Classifier containerised with Docker and deployed to AWS ECR via GitHub Actions CI/CD pipeline.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-REST_API-000000?logo=flask)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-Containerised-2496ED?logo=docker)](https://docker.com)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions)](https://github.com/features/actions)
[![AWS ECR](https://img.shields.io/badge/AWS-ECR-FF9900?logo=amazonaws)](https://aws.amazon.com/ecr)
[![Status](https://img.shields.io/badge/Status-Deployed%20%26%20Verified-2ea44f)]()

---

## What This Project Does

A Flask REST API serving an AI-powered spam classification model, fully containerised
with Docker and delivered via an automated GitHub Actions CI/CD pipeline. Every push to
main triggers automatic linting, testing, Docker image build, and push to AWS ECR —
zero manual deployment steps. Demonstrates the complete DevOps software delivery lifecycle
from code commit to production-ready container in a cloud registry.

---

## Architecture

```
  DEVELOPER                  GITHUB ACTIONS              AWS CLOUD
  ──────────               ──────────────────           ───────────
  git push                                              ┌──────────┐
      │                    ┌──────────────┐             │  AWS ECR  │
      └──► GitHub ────────►│  Lint Code   │             │ Registry │
                           │  flake8      │             └────┬─────┘
                           └──────┬───────┘                  │
                                  │                          │
                           ┌──────▼───────┐                  │
                           │  Run Tests   │                  │
                           │  pytest      │                  │
                           └──────┬───────┘                  │
                                  │                          │
                           ┌──────▼───────┐                  │
                           │ Build Docker │                  │
                           │   Image      │                  │
                           └──────┬───────┘                  │
                                  │                          │
                           ┌──────▼───────┐                  │
                           │  Push to ECR │──────────────────┘
                           └──────────────┘
```

---

## CI/CD Pipeline Stages

| Stage | Tool | What Happens |
|---|---|---|
| Trigger | GitHub Actions | Fires on every push to `main` branch |
| Lint | flake8 | Checks Python code quality and style |
| Test | pytest | Runs automated unit tests |
| Build | Docker | Builds container image from Dockerfile |
| Push | AWS ECR | Pushes versioned image to private registry |

---

## Components

| Component | Technology | Purpose |
|---|---|---|
| Web Framework | Flask | REST API serving classification predictions |
| ML Model | scikit-learn | Spam vs ham text classifier |
| Container | Docker | Portable, environment-agnostic packaging |
| CI/CD | GitHub Actions | Automated build, test, and deploy pipeline |
| Registry | AWS ECR | Private container image storage |
| Tests | pytest | Automated validation of model and API |

---

## Security Design

- **AWS ECR private registry** — images not publicly accessible, IAM-controlled
- **GitHub Actions secrets** — AWS credentials stored as encrypted repository secrets, never in code
- **Docker non-root user** — container runs as non-root for reduced attack surface
- **Dependency scanning** — CI pipeline checks for known vulnerabilities in requirements

---

## Key Design Decisions

**Why GitHub Actions over Jenkins?**
GitHub Actions is native to the repository — no separate CI server to manage.
Workflow YAML lives in the repo, is version-controlled, and runs on GitHub-managed
infrastructure. Zero maintenance overhead for a portfolio-scale project.

**Why AWS ECR over Docker Hub?**
ECR integrates natively with AWS IAM — no separate registry credentials needed when
pulling from ECS, EKS, or EC2. Images are private by default. This is the production
pattern used at enterprise scale.

**Why containerise the ML model?**
A model that only runs on one machine is not production-ready. Docker makes the model
plus all its dependencies portable — runs identically on a developer laptop, a CI runner,
and a production EC2 instance. This is the foundation of MLOps.

**Why automated tests before Docker build?**
The pipeline fails fast — if tests fail, the Docker build never runs, and no broken image
reaches ECR. This prevents bad code from polluting the container registry.

---

## Quick Start

```bash
# Clone
git clone https://github.com/sadvi11/docker-flask-ai-app.git
cd docker-flask-ai-app

# Run locally with Docker
docker build -t flask-ai-app .
docker run -p 5000:5000 flask-ai-app

# Or with Docker Compose
docker-compose up

# Test the API
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Congratulations! You have won a free prize!"}'
```

---

## Repository Structure

```
docker-flask-ai-app/
├── app/
│   ├── app.py              # Flask REST API
│   └── model.py            # Spam classifier model
├── tests/
│   └── test_app.py         # pytest test suite
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD pipeline
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Local development orchestration
├── requirements.txt        # Python dependencies
├── screenshots/            # Deployment proof
├── WHY.md                  # Design decision documentation
└── README.md
```

---

## Interview Talking Points

- **CI/CD pipeline design** — what each stage does and why the order matters
- **Docker multi-stage builds** — how to reduce image size for production
- **GitHub Actions secrets** — how to store AWS credentials securely in pipelines
- **AWS ECR lifecycle policies** — how to manage image retention and cost
- **Testing in CI** — why tests must pass before build, not after
- **Container security** — non-root users, image scanning, minimal base images

---

## Author

**Sadhvi Sharma** — Cloud & AI Engineer
Nokia India (5G Packet Core) → Cloud & AI Engineering
Calgary, AB, Canada | Permanent Resident | Open to Relocation

[LinkedIn](https://linkedin.com/in/sadhvi-sharma-5789a6249) | [GitHub](https://github.com/sadvi11)
