from fastapi.testclient import TestClient

from app import __version__
from app.config import Settings, get_settings
from app.main import create_app


def test_health_returns_versions_in_camel_case() -> None:
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(
        model_version="m-test", data_version="d-test"
    )

    res = TestClient(app).get("/health")

    assert res.status_code == 200
    assert res.json() == {
        "status": "UP",
        "version": __version__,
        "modelVersion": "m-test",
        "dataVersion": "d-test",
    }
