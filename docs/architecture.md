# CI/CD Platform Architecture

## Workflow

Developer
↓
Git Push
↓
GitHub Repository
↓
GitHub Actions

1. Lint Stage
   - Black
   - Flake8

2. Security Scan
   - Trivy Filesystem Scan

3. Test Stage
   - Pytest

4. Docker Build Stage
   - Multi-stage Docker Build

↓

Docker Image Validation

## Container Features

- Multi-stage Docker build
- Non-root container execution
- Gunicorn WSGI server
- Docker HEALTHCHECK
- Flask application health endpoint
