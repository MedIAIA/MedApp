import pytest
from digiez_api import db as db_, create_app
from digiez_api.config import EnvConfig

@pytest.fixture(scope='session')
def app(request):
    EnvConfig.SQLALCHEMY_DATABASE_URI = EnvConfig.TEST_DATABASE_URI
    EnvConfig.TESTING = True
    # App Creation
    app_ = create_app('config')

    # Establish an application context before running the tests.
    ctx = app_.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app_
