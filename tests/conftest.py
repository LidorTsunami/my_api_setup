import pytest

import elements
from api.api_client import APIClient


@pytest.fixture()
def api_client():
    yield APIClient(base_url=elements.api_base_url)

