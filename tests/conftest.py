import pytest

from walmart import Walmart
from .mocks import get_mock_for


@pytest.fixture
def walmart(requests_mock):
    requests_mock.post(
        "https://marketplace.walmartapis.com/v3/token",
        json=get_mock_for("token")
    )
    walmart = Walmart(
        client_id="client_id",
        client_secret="client_secret",
    )
    return walmart
