import pytest

import elements
from api.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    yield APIClient(base_url=elements.API_BASE_URL)
