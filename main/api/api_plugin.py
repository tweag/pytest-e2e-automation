import os

import pytest


@pytest.fixture
def driver():
    return


@pytest.fixture(scope="session")
def api_base_url():
    """Fixture to set the API Base URL from environment variable"""
    return os.environ.get("API_BASE_URL")
