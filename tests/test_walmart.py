#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_walmart
----------------------------------
Tests for `walmart` module.
"""

import pytest  # noqa

from .mocks import get_mock_for


def test_token_generation(walmart):
    "test if token authentication call is made"
    assert walmart.token is not None
    assert walmart.token_expires_in is not None


def test_items_all(walmart, requests_mock):
    "test fetching all items"
    requests_mock.get(
        "https://marketplace.walmartapis.com/v3/items",
        json=get_mock_for("items")
    )
    response = walmart.items.all()
    items = response["ItemResponse"]
    assert len(items) == 20

    assert items[0]["mart"] == "WALMART_US"
    assert items[0]["sku"] == "101013-21550015340"
    assert items[0]["gtin"] == "00635510505068"

    assert items[1]["mart"] == "WALMART_US"
    assert items[1]["sku"] == "101010-43805580"
    assert items[1]["gtin"] == "00635510489702"


def test_orders_all(walmart, requests_mock):
    "test fetching all orders"
    requests_mock.get(
        "https://marketplace.walmartapis.com/v3/orders?"
        "createdStartDate=2019-07-19T00:00:00Z&limit=5",
        json=get_mock_for("orders")
    )
    response = walmart.orders.all(
        createdStartDate="2019-07-19T00:00:00Z",
        limit=5
    )
    orders = response["list"]["elements"]["order"]
    assert len(orders) == 5

    assert orders[0]["purchaseOrderId"] == "4792059978801"
    assert orders[0]["customerOrderId"] == "4751966035239"
    assert len(orders[0]["orderLines"]["orderLine"]) == 3

    assert orders[1]["purchaseOrderId"] == "4792059978430"
    assert orders[1]["customerOrderId"] == "4751966531767"
    assert len(orders[1]["orderLines"]["orderLine"]) == 1
