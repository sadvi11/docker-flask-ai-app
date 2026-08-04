# Why I Built This Project

## Real World Problem This Solves

Any organisation handling inbound messages at volume runs into the same wall: the
message count grows and the reviewing headcount cannot grow with it. Manual triage is
accurate and does not scale; no triage at all is cheap and floods the people downstream.

The practical answer is a classifier that handles the confident majority automatically and
escalates only what it is unsure about — so human attention goes to the ambiguous cases
instead of the obvious ones.

This project solves that with a containerized AI service.
Any team can deploy it anywhere with one command.

## Why Docker Specifically

Without Docker:
- App works on my Mac
- Crashes on Linux server
- Different Python versions cause errors
- Deployment takes days

With Docker:
- One image runs everywhere
- Zero environment conflicts
- Deployment takes seconds
- Same behavior on every machine

## Nokia Connection

At Nokia network functions ran in isolated containers.
AMF, SMF, UPF each ran in separate isolated environments.
Same concept as Docker containers.
Each function isolated, controlled interfaces between them.

## What I Learned

- Dockerfile - how to package a complete application
- Docker layers - efficient image caching
- Port mapping - connecting host to container
- AWS ECR - production container registry
- GitHub Actions - automated build and push pipeline
- docker-compose - running multi-container apps

## Interview Answer

I containerized an AI Flask application using Docker and
deployed it to AWS ECR with an automated GitHub Actions pipeline.

The container packages Python, Flask, scikit-learn and the
AI model together - runs identically on any machine.

This solves the works on my machine problem that costs
Canadian companies millions in wasted engineering hours.

## Cost
Docker - free
AWS ECR - 500MB free tier
GitHub Actions - 2000 minutes free
Total - zero
