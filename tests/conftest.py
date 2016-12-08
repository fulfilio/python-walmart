import os
import pytest
import responses
from walmart import Walmart


@pytest.fixture
def fp():
    def wrapper(rel_path):
        "return the full path of given rel_path"
        return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                rel_path
            )
        )
    return wrapper


@pytest.fixture
def walmart():
    private_key= """MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKzXEfCYdnBNkKAwVbCpg/tR40WixoZtiuEviSEi4+LdnYAAPy57Qw6+9eqJGTh9iCB2wP/I8lWh5TZ49Hq/chjTCPeJiOqi6bvX1xzyBlSq2ElSY3iEVKeVoQG/5f9MYQLEj5/vfTWSNASsMwnNeBbbHcV1S1aY9tOsXCzRuxapAgMBAAECgYBjkM1j1OA9l2Ed9loWl8BQ8X5D6h4E6Gudhx2uugOe9904FGxRIW6iuvy869dchGv7j41ki+SV0dpRw+HKKCjYE6STKpe0YwIm/tml54aNDQ0vQvF8JWILca1a7v3Go6chf3Ib6JPs6KVsUuNo+Yd+jKR9GAKgnDeXS6NZlTBUAQJBANex815VAySumJ/n8xR+h/dZ2V5qGj6wu3Gsdw6eNYKQn3I8AGQw8N4yzDUoFnrQxqDmP3LOyr3/zgOMNTdszIECQQDNIxiZOVl3/Sjyxy9WHMk5qNfSf5iODynv1OlTG+eWao0Wj/NdfLb4pwxRsf4XZFZ1SQNkbNne7+tEO8FTG1YpAkAwNMY2g/ty3E6iFl3ea7UJlBwfnMkGz8rkye3F55f/+UCZcE2KFuIOVv4Kt03m3vg1h6AQkaUAN8acRl6yZ2+BAkEAke2eiRmYANiR8asqjGqr5x2qcm8ceiplXdwrI1kddQ5VUbCTonSewOIszEz/gWp6arLG/ADHOGWaCo8rptAyiQJACXd1ddXUAKs6x3l752tSH8dOde8nDBgF86NGvgUnBiAPPTmJHuhWrmOZmNaB68PsltEiiFwWByGFV+ld9VKmKg=="""  # noqa
    walmart = Walmart(
        consumer_id='CONSUMER_ID',
        channel_type='CHANNEL_TYPE',
        private_key=private_key
    )
    walmart.base_url = 'http://mywalmart/api/v2/%s'
    return walmart


@pytest.yield_fixture
def resp(fp):
    rsps = responses.RequestsMock(False)
    rsps.start()

    "Items"
    rsps.add(
        responses.GET,
        'http://mywalmart/api/v2/items',
        body=open(fp('responses/items.xml'), 'r').read()
    )
    "Orders"
    rsps.add(
        responses.GET,
        'http://mywalmart/api/v2/orders',
        body=open(fp('responses/orders.xml'), 'r').read()
    )
    yield rsps

    rsps.stop()
    rsps.reset()
