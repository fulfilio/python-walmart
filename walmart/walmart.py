# -*- coding: utf-8 -*-
import requests
import base64
import time
from uuid import uuid4
from lxml import etree
from lxml.builder import E, ElementMaker
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Walmart(object):

    def __init__(self, consumer_id, channel_type, private_key):
        self.base_url = 'https://marketplace.walmartapis.com/v2/%s'
        self.consumer_id = consumer_id
        self.channel_type = channel_type
        self.private_key = private_key
        self.session = requests.Session()
        self.session.headers['Accept'] = 'application/xml'
        self.session.headers['WM_SVC.NAME'] = 'Walmart Marketplace'
        self.session.headers['WM_CONSUMER.ID'] = self.consumer_id
        self.session.headers['WM_CONSUMER.CHANNEL.TYPE'] = self.channel_type

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

    def get_sign(self, url, method, timestamp):
        return self.sign_data(
            '\n'.join([self.consumer_id, url, method, timestamp]) + '\n'
        )

    def sign_data(self, data):
        rsakey = RSA.importKey(base64.b64decode(self.private_key))
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA256.new()
        digest.update(data.encode('utf-8'))
        sign = signer.sign(digest)
        return base64.b64encode(sign)

    def get_headers(self, url, method):
        timestamp = str(int(round(time.time() * 1000)))
        return {
            'WM_SEC.AUTH_SIGNATURE': self.get_sign(url, method, timestamp),
            'WM_SEC.TIMESTAMP': timestamp,
            'WM_QOS.CORRELATION_ID': str(uuid4()),
        }

    def send_request(self, method, url, params=None, body=None):
        encoded_url = url
        if params:
            encoded_url += '?%s' % urlencode(params)
        headers = self.get_headers(encoded_url, method)

        if method == 'GET':
            return self.session.get(url, params=params, headers=headers)
        elif method == 'PUT':
            return self.session.put(url, params=params, headers=headers)
        elif method == 'POST':
            return self.session.post(url, data=body, headers=headers)


class Resource(object):
    """
    A base class for all Resources to extend
    """

    def __init__(self, connection):
        self.connection = connection

    @property
    def url(self):
        return self.connection.base_url % self.path

    def all(self, **kwargs):
        return self.connection.send_request(
            method='GET', url=self.url, params=kwargs)

    def get(self, id):
        url = self.url + '/%s' % id
        return self.connection.send_request(method='GET', url=url)

    def update(self, **kwargs):
        return self.connection.send_request(
            method='PUT', url=self.url, params=kwargs)

    def bulk_update(self, items):
        url = self.connection.base_url % 'feeds?feedType=%s' % self.feedType
        return self.connection.send_request(
            method='POST', url=url, data=self.get_payload(items))


class Items(Resource):
    """
    Get all items
    """

    path = 'items'


class Inventory(Resource):
    """
    Retreives inventory of an item
    """

    path = 'inventory'
    feedType = 'inventory'

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
