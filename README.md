# Dockerized Flask AI Spam Classifier

## What This Project Does
AI-powered spam detection service running in Docker container.
Deployed to AWS ECR with automated CI/CD via GitHub Actions.
One command runs the entire service anywhere in the world.

## Architecture
Flask AI App + scikit-learn model
        |
Docker Container
        |
AWS ECR - cloud image registry
        |
GitHub Actions - auto builds on every push

## API Endpoints
GET  /health   - health check
GET  /         - service info
POST /predict  - classify text as SPAM or HAM

## Example
curl -X POST http://localhost:5001/predict
-H "Content-Type: application/json"
-d '{"text": "Win free money now"}'

Response: {"prediction": "SPAM", "confidence": 99.75}

## Tech Stack
Docker | Flask | scikit-learn | AWS ECR | GitHub Actions | Python

## How to Run Locally
docker build -t spam-classifier-ai .
docker run -d -p 5001:5000 spam-classifier-ai
curl http://localhost:5001/health

## Cost
AWS ECR free tier - 500MB per month free
GitHub Actions - 2000 minutes per month free
Total cost - zero

## Screenshots
(screenshots folder coming soon)
