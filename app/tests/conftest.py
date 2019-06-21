import pytest
from app import create_app


@pytest.fixture
def app():

    app = create_app()
    app.secret_key = 'some secret'
    return app

