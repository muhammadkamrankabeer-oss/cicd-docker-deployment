from app.app import app


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "CI/CD Docker Deployment Platform"
    assert data["status"] == "running"


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_version_endpoint():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200

    data = response.get_json()

    assert data["version"] == "1.0.0"
