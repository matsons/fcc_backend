import time
import pytest
from dtuservice import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    with app.app_context():
        pass
        # We'll need to do something with this in a bit...
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()