# CI/CD Docker Deployment - Interview Questions

## 1. What is CI/CD?

CI (Continuous Integration) is the practice of automatically validating code changes through testing and quality checks.

CD (Continuous Delivery/Deployment) automates the process of delivering software after successful validation.

---

## 2. Why use GitHub Actions?

GitHub Actions provides native CI/CD capabilities integrated directly into GitHub repositories.

Benefits:

- Automated testing
- Automated builds
- Workflow as code
- Easy integration with GitHub

---

## 3. What happens when code is pushed to main?

The GitHub Actions workflow starts automatically.

Stages:

1. Lint
2. Security Scan
3. Test
4. Docker Build

If any stage fails, the pipeline stops.

---

## 4. Why use Black?

Black enforces a consistent Python coding style.

Benefits:

- Standard formatting
- Cleaner code reviews
- Reduced style discussions

---

## 5. Why use Flake8?

Flake8 performs static code analysis.

It detects:

- Style violations
- Unused imports
- Potential coding mistakes

---

## 6. Why use Trivy?

Trivy scans source code, dependencies, and container images for vulnerabilities.

Benefits:

- Early security detection
- DevSecOps integration
- Automated security validation

---

## 7. What is a multi-stage Docker build?

A multi-stage build separates build dependencies from runtime dependencies.

Benefits:

- Smaller image size
- Better security
- Faster deployments

---

## 8. Why run containers as non-root?

Running containers as root increases security risks.

Using a dedicated application user follows the principle of least privilege.

---

## 9. What is a Docker HEALTHCHECK?

A HEALTHCHECK verifies whether the application inside the container is functioning correctly.

Benefits:

- Health monitoring
- Faster failure detection
- Better orchestration support

---

## 10. Why use Gunicorn instead of Flask development server?

Gunicorn is a production-grade WSGI server.

Benefits:

- Better performance
- Multiple workers
- Production readiness

---

## 11. Why use Vagrant in this project?

Vagrant provides a reproducible development environment.

Benefits:

- Consistent setup
- Easy onboarding
- Infrastructure reproducibility

---

## 12. What DevOps concepts does this project demonstrate?

- Continuous Integration
- DevSecOps
- Infrastructure Automation
- Containerization
- Automated Testing
- Secure Software Delivery
