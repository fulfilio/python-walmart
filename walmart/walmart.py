# -*- coding: utf-8 -*-
import requests
import uuid
import csv
import io
import zipfile

from requests.auth import HTTPBasicAuth
from lxml import etree
from lxml.builder import E, ElementMaker

from .exceptions import WalmartAuthenticationError


class Walmart(object):

    def __init__(self, client_id, client_secret):
        """To get client_id and client_secret for your Walmart Marketplace
        visit: https://developer.walmart.com/#/generateKey
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.token_expires_in = None
        self.base_url = "https://marketplace.walmartapis.com/v3"

        session = requests.Session()
        session.headers.update({
            "WM_SVC.NAME": "Walmart Marketplace",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        })
        session.auth = HTTPBasicAuth(self.client_id, self.client_secret)
        self.session = session

        # Get the token required for API requests
        self.authenticate()

    def authenticate(self):
        response = self.send_request(
            "POST", "{}/token".format(self.base_url),
            body={
                "grant_type": "client_credentials",
            },
        )
        data = response.json()
        self.token = data["access_token"]
        self.token_expires_in = data["expires_in"]

        self.session.headers["WM_SEC.ACCESS_TOKEN"] = self.token

    @property
    def items(self):
        return Items(connection=self)

    @property
    def inventory(self):
        return Inventory(connection=self)

    @property
    def prices(self):
        return Prices(connection=self)

    @property
    def orders(self):
        return Orders(connection=self)

    @property
    def report(self):
        return Report(connection=self)

    def send_request(
        self, method, url, params=None, body=None, request_headers=None
    ):
        # A unique ID which identifies each API call and used to track
        # and debug issues; use a random generated GUID for this ID
        headers = {
            "WM_QOS.CORRELATION_ID": uuid.uuid4().hex,
        }
        if request_headers:
            headers.update(request_headers)

        response = None
        if method == "GET":
            response = self.session.get(url, params=params, headers=headers)
        elif method == "PUT":
            response = self.session.put(
                url, params=params, headers=headers, data=body
            )
        elif method == "POST":
            response = self.session.post(url, data=body, headers=headers)

        if response is not None:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                if response.status_code == 401:
                    raise WalmartAuthenticationError((
                        "Invalid client_id or client_secret. Please verify "
                        "your credentials from https://developer.walmart."
                        "com/#/generateKey"
                    ))
                elif response.status_code == 400:
                    data = response.json()
                    if data["error"][0]["code"] == \
                            "INVALID_TOKEN.GMP_GATEWAY_API":
                        # Refresh the token as the current token has expired
                        self.authenticate()
                        return self.send_request(
                            method, url, params, body, request_headers
                        )
                raise
        return response


class Resource(object):
    """
    A base class for all Resources to extend
    """

    def __init__(self, connection):
        self.connection = connection

    @property
    def url(self):
        return "{}/{}".format(self.connection.base_url, self.path)

    def all(self, **kwargs):
        return self.connection.send_request(
            method="GET", url=self.url, params=kwargs
        )

    def get(self, id):
        url = "{}/{}".format(self.url, id)
        return self.connection.send_request(method="GET", url=url)

    def update(self, **kwargs):
        return self.connection.send_request(
            method="PUT", url=self.url, params=kwargs
        )

    def bulk_update(self, items):
        url = self.connection.base_url % 'feeds?feedType=%s' % self.feedType
        boundary = uuid.uuid4().hex
        headers = {
            'Content-Type': "multipart/form-data; boundary=%s" % boundary
        }
        data = self.get_payload(items)
        body = '--{boundary}\n\n{data}\n--{boundary}--'.format(
            boundary=boundary, data=data
        )
        return self.connection.send_request(
            method='POST',
            url=url,
            body=body,
            request_headers=headers
        )


class Items(Resource):
    """
    Get all items
    """

    path = 'items'

    def get_items(self):
        "Get all the items from the Item Report"
        response = self.connection.report.all(type="item")
        zf = zipfile.ZipFile(io.BytesIO(response.content), "r")
        product_report = zf.read(zf.infolist()[0]).decode("utf-8")

        return list(csv.DictReader(io.StringIO(product_report)))


class Inventory(Resource):
    """
    Retreives inventory of an item
    """

    path = 'inventory'
    feedType = 'inventory'

    def update_inventory(self, sku, quantity):
        headers = {
            'Content-Type': "application/xml"
        }
        return self.connection.send_request(
            method='PUT',
            url=self.url,
            params={'sku': sku},
            body=self.get_inventory_payload(sku, quantity),
            request_headers=headers
        )

    def get_inventory_payload(self, sku, quantity):
        element = ElementMaker(
            namespace='http://walmart.com/',
            nsmap={
                'wm': 'http://walmart.com/',
            }
        )
        return etree.tostring(
            element(
                'inventory',
                element('sku', sku),
                element(
                    'quantity',
                    element('unit', 'EACH'),
                    element('amount', str(quantity)),
                ),
                element('fulfillmentLagTime', '4'),
            ), xml_declaration=True, encoding='utf-8'
        )

    def get_payload(self, items):
        return etree.tostring(
            E.InventoryFeed(
                E.InventoryHeader(E('version', '1.4')),
                *[E(
                    'inventory',
                    E('sku', item['sku']),
                    E(
                        'quantity',
                        E('unit', 'EACH'),
                        E('amount', item['quantity']),
                    )
                ) for item in items],
                xmlns='http://walmart.com/'
            )
        )


class Prices(Resource):
    """
    Retreives price of an item
    """

    path = 'prices'
    feedType = 'price'

    def get_payload(self, items):
        root = ElementMaker(
            nsmap={'gmp': 'http://walmart.com/'}
        )
        return etree.tostring(
            root.PriceFeed(
                E.PriceHeader(E('version', '1.5')),
                *[E.Price(
                    E(
                        'itemIdentifier',
                        E('sku', item['sku'])
                    ),
                    E(
                        'pricingList',
                        E(
                            'pricing',
                            E(
                                'currentPrice',
                                E(
                                    'value',
                                    **{
                                        'currency': item['currenctCurrency'],
                                        'amount': item['currenctPrice']
                                    }
                                )
                            ),
                            E('currentPriceType', item['priceType']),
                            E(
                                'comparisonPrice',
                                E(
                                    'value',
                                    **{
                                        'currency': item['comparisonCurrency'],
                                        'amount': item['comparisonPrice']
                                    }
                                )
                            ),
                            E(
                                'priceDisplayCode',
                                **{
                                    'submapType': item['displayCode']
                                }
                            ),
                        )
                    )
                ) for item in items]
            ), xml_declaration=True, encoding='utf-8'
        )


class Orders(Resource):
    """
    Retrieves Order details
    """

    path = 'orders'

    def acknowledge(self, id):
        url = self.url + '/%s/acknowledge' % id
        return self.send_request(method='POST', url=url)

    def cancel(self, id, lines):
        url = self.url + '/%s/cancel' % id
        return self.send_request(
            method='POST', url=url, data=self.get_cancel_payload(lines))

    def get_cancel_payload(self, lines):
        element = ElementMaker(
            namespace='http://walmart.com/mp/orders',
            nsmap={
                'ns2': 'http://walmart.com/mp/orders',
                'ns3': 'http://walmart.com/'
            }
        )
        return etree.tostring(
            element(
                'orderCancellation',
                element(
                    'orderLines',
                    *[element(
                        'orderLine',
                        element('lineNumber', line),
                        element(
                            'orderLineStatuses',
                            element(
                                'orderLineStatus',
                                element('status', 'Cancelled'),
                                element(
                                    'cancellationReason', 'CANCEL_BY_SELLER'),
                                element(
                                    'statusQuantity',
                                    element('unitOfMeasurement', 'EACH'),
                                    element('amount', '1')
                                )
                            )
                        )
                    ) for line in lines]
                )
            ), xml_declaration=True, encoding='utf-8'
        )

    def update_shipment(self, order_id, package):
        headers = {
            'Content-Type': "application/xml"
        }
        url = self.url + '/%s/shipping' % order_id
        return self.connection.send_request(
            method='POST',
            url=url,
            body=self.get_shipment_payload(package),
            request_headers=headers
        )

    def get_shipment_payload(self, package):
        """Shipment Update

        :param package: {
            "tracking_number": "",
            "tracking_url": "",
            "carrier": "",
            "carrier_service": '',
            "ship_date_time": '',
            "items": [{
                "line_number": "",
                "quantity": 2,
                "status": "Shipped",
                "uom": "Each",
            }]
        }
        """
        element = ElementMaker(
            namespace='http://walmart.com/mp/v3/orders',
            nsmap={
                'ns2': 'http://walmart.com/mp/v3/orders',
                'ns3': 'http://walmart.com/'
            }
        )
        order_lines = []
        for item in package['items']:
            tracking_info = element(
                'trackingInfo',
                element('shipDateTime', package.get('ship_date_time', '')),
                element('carrierName', element('carrier', package['carrier'])),
                element('methodCode', package['carrier_service']),
                element('trackingNumber', package['tracking_number']),
                element('trackingURL', package.get('tracking_url', '')),
            )
            status_info = element(
                'orderLineStatuses',
                element(
                    'orderLineStatus',
                    element('status', item['status']),
                    element(
                        'statusQuantity',
                        element('unitOfMeasurement', item['uom']),
                        element('amount', str(item['quantity']))
                    ),
                    tracking_info
                )
            )
            order_lines.append(element(
                'orderLine',
                element('lineNumber', item['line_number']),
                status_info
            ))
        shipment_data = element(
            'orderShipment', element('orderLines', *order_lines)
        )
        return etree.tostring(
            shipment_data, xml_declaration=True, encoding='utf-8'
        )


class Report(Resource):
    """
    Get report
    """

    path = 'getReport'
