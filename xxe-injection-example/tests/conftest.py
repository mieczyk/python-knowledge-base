# When pytest does test discovery, all conftest.py files found 
# will be run during the test collection phase (before any tests are run).
# No explicit imports are required.

import pytest

from ..app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
