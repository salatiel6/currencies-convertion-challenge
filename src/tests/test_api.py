import pytest
import sys
sys.path.insert(1, "../")

from controllers import app # noqa


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_home(client):
    url = "/home"
    result = client.get(url)

    assert result.status_code == 200
