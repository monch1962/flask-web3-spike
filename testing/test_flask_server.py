import pytest
from app import MyApp

@pytest.fixture
def client():
    app = MyApp()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_version():
    resp = client.get('/version')
    assert resp.status_code == 200