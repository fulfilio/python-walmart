#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_walmart
----------------------------------
Tests for `walmart` module.
"""

import pytest 	# noqa
from lxml import objectify


def test_items_all(resp, walmart):
    "test fetching all items"
    response = walmart.items.all()
    items = objectify.fromstring(response.content)
    assert items.MPItemView[0].mart == 'WALMART_US'
    assert items.MPItemView[0].sku == '1701-810'
    assert items.MPItemView[0].gtin == 635510465225


def test_orders_all(resp, walmart):
    "test fetching all orders"
    response = walmart.orders.all(createdStartDate='2016-12-06')
    orders = objectify.fromstring(response.content)
    assert orders.elements.order.purchaseOrderId == 1234567890
    assert orders.elements.order.customerOrderId == 987654321
    assert orders.elements.order.customerEmailId == 'brucewayne@gmail.com'
