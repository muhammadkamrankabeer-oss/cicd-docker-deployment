# 🚀 CI/CD Docker Deployment

A hands-on DevOps lab demonstrating a complete **CI/CD pipeline** for a containerized Python (Flask) application — from local Vagrant provisioning, through automated testing in GitHub Actions, to a multi-stage Docker build pushed straight to Docker Hub.

<p>
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-black?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-Multi--stage%20Build-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/Tested%20with-Pytest-0A9EDC?logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Provisioned%20with-Vagrant-1868F2?logo=vagrant&logoColor=white" alt="Vagrant">
</p>

---

## 📐 Architecture

```
 Developer Machine                GitHub                         Docker Hub
┌──────────────────┐      ┌─────────────────────┐          ┌──────────────────┐
│  Vagrant VM       │      │  GitHub Actions CI  │          │                  │
│  (Debian 12)      │ push │ ┌──────────────────┐│  push    │   cicd-app:latest│
│  + Docker Engine   │────▶│ │ 1. validate       ││  image   │                  │
│                    │      │ │ 2. test (pytest)  ││─────────▶│                  │
│  Flask App :5000   │      │ │ 3. build & push   ││          │                  │
└──────────────────┘      │ └──────────────────┘│          └──────────────────┘
                            └─────────────────────┘
```

The Vagrant box mirrors a clean Debian server with Docker pre-installed, so the app can be built and run identically on a laptop or a VPS. Every push to `main` then triggers the same build inside GitHub Actions, runs the test suite, and — on success — publishes the image to Docker Hub.

---

## ✨ Features

- 🐍 Minimal Flask web app with a single health-check style route
- 🧪 Automated unit testing with `pytest` and Flask's test client
- 🐳 Multi-stage `Dockerfile` — slim runtime image, non-root user, served via `gunicorn`
- 📦 Reproducible dev environment via `Vagrant` + VirtualBox (Debian 12 "bookworm")
- ⚙️ 3-stage GitHub Actions pipeline: **validate → test → build & push**
- 🔐 Docker Hub credentials handled securely via GitHub Actions secrets
- 🖼️ Screenshots documenting each stage of the workflow

---

## 🛠️ Tech Stack

| Layer              | Tool / Technology              |
|--------------------|---------------------------------|
| Application         | Python 3.10, Flask              |
| WSGI Server          | Gunicorn                        |
| Testing              | Pytest                          |
| Containerization     | Docker (multi-stage build)      |
| Local Infrastructure | Vagrant + VirtualBox (Debian 12)|
| CI/CD                | GitHub Actions                  |
| Image Registry       | Docker Hub                      |

---

## 📂 Project Structure

```
cicd-docker-deployment/
├── .github/workflows/
│   └── ci.yml              # CI/CD pipeline: validate, test, build & push
├── app/
│   ├── __init__.py
│   └── app.py               # Flask application
├── docker/
│   └── Dockerfile           # Multi-stage build, non-root user, gunicorn
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Pytest test suite
├── screenshots/             # Workflow screenshots
├── requirements.txt         # flask, gunicorn, pytest
├── Vagrantfile               # Debian 12 VM with Docker pre-installed
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites
- [Vagrant](https://www.vagrantup.com/) + [VirtualBox](https://www.virtualbox.org/) (for the local VM workflow)
- Docker (installed automatically inside the VM, or locally on your machine)
- Python 3.10+

### 1. Spin up the VM (optional, mirrors a clean server)
```bash
vagrant up
vagrant ssh
cd /home/vagrant/cicd-project
```

### 2. Run tests locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

### 3. Build and run with Docker
```bash
docker build -t cicd-app -f docker/Dockerfile .
docker run -d -p 5000:5000 cicd-app
```

Visit **http://localhost:5000** (or **http://192.168.56.10:5000** if running inside the Vagrant VM) — you should see:

```
CI/CD Pipeline Working 🚀
```

---

## 🔄 CI/CD Pipeline

Defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml), the pipeline runs on every push or pull request to `main`:

| Stage      | What it does                                                            |
|------------|---------------------------------------------------------------------------|
| **validate** | Checks out the code and confirms the Dockerfile exists                |
| **test**     | Sets up Python, installs dependencies in a virtualenv, runs `pytest`   |
| **build**    | Logs in to Docker Hub and builds + pushes `cicd-app:latest` (depends on `test` passing) |

Docker Hub credentials are read from the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` repository secrets — no credentials are stored in the codebase.

---

## 🖼️ Screenshots

| | |
|---|---|
| VM provisioned (`vagrant up`) | SSH into VM |
| ![vm up](screenshots/vm-up.png) | ![vm ssh](screenshots/vm-ssh.png) |
| Docker installed in VM | Docker image build |
| ![docker install](screenshots/docker-install.png) | ![docker build](screenshots/docker-build.png) |
| Container running | Tests passing |
| ![docker run](screenshots/docker-run.png) | ![tests pass](screenshots/tests-pass.png) |
| App in browser | |
| ![app browser](screenshots/app-browser.png) | |

---

## 🧭 Possible Next Steps

- Add a `/health` endpoint and container `HEALTHCHECK`
- Tag images with the Git commit SHA in addition to `latest`
- Add a deploy stage (e.g. to a VPS or Kubernetes) after the image is pushed
- Add `flake8`/`black` to the validate stage for real linting

---

## 👤 Author

**Muhammad Kamran Kabeer**
IT Lab Manager · DevOps Engineer · Lecturer

<p>
  <a href="https://www.devriston.com.pk"><img src="https://img.shields.io/badge/Website-devriston.com.pk-0A66C2?style=for-the-badge" alt="Website"></a>
  <a href="https://www.linkedin.com/in/kamrankabeer/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/muhammadkamrankabeer-oss"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
</p>
