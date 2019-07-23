# flake8:noqa


def get_mock_for(resource):
    if resource == "token":
        return {
            "access_token": "token",
            "token_type": "Bearer",
            "expires_in": 900
        }
    elif resource == "orders":
        return {
            'list': {
                'meta': {
                    'totalCount': 35,
                    'limit': 5,
                    'nextCursor': '?limit=5&hasMoreElements=true&soIndex=35&poIndex=5&partnerId=10000004040&sellerId=4010&createdStartDate=2019-07-19T00:00:00Z&createdEndDate=2019-07-23T11:52:53.226Z'
                },
                'elements': {
                    'order': [{
                            'purchaseOrderId': '4792059978801',
                            'customerOrderId': '4751966035239',
                            'customerEmailId': '257050E418F3443DB6C22D63EBAE015D@relay.walmart.com',
                            'orderDate': 1563859433000,
                            'shippingInfo': {
                                'phone': '2563384465',
                                'estimatedDeliveryDate': 1565031600000,
                                'estimatedShipDate': 1564459200000,
                                'methodCode': 'Standard',
                                'postalAddress': {
                                    'name': 'Leslie Rushing',
                                    'address1': '2421 County Road 310',
                                    'address2': None,
                                    'city': 'Crane Hill',
                                    'state': 'AL',
                                    'postalCode': '35053',
                                    'country': 'USA',
                                    'addressType': 'RESIDENTIAL'
                                }
                            },
                            'orderLines': {
                                'orderLine': [{
                                        'lineNumber': '3',
                                        'item': {
                                            'productName': '3/8" Grosgrain Ribbon Solid 235 Poppy Red 5yd',
                                            'sku': '101010-43805235'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.89
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.07
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.98
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.08
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563872584000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    },
                                    {
                                        'lineNumber': '4',
                                        'item': {
                                            'productName': '3/8" Grosgrain Ribbon Solid 156 Hot Pink 5yd',
                                            'sku': '101010-43805156'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.89
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.07
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.99
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.08
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563872584000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    },
                                    {
                                        'lineNumber': '5',
                                        'item': {
                                            'productName': '3/8" Grosgrain Ribbon Solid 030 Black 5yd',
                                            'sku': '101010-43805030'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.89
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.07
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.98
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.08
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563872584000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            'purchaseOrderId': '4792059978430',
                            'customerOrderId': '4751966531767',
                            'customerEmailId': '634259E9C72A4D43B608B16B830E6738@relay.walmart.com',
                            'orderDate': 1563859348000,
                            'shippingInfo': {
                                'phone': '3056008814',
                                'estimatedDeliveryDate': 1565031600000,
                                'estimatedShipDate': 1564459200000,
                                'methodCode': 'Standard',
                                'postalAddress': {
                                    'name': 'Joie Simpkins',
                                    'address1': '6603 nw 2nd pl',
                                    'address2': None,
                                    'city': 'Miami',
                                    'state': 'FL',
                                    'postalCode': '33150',
                                    'country': 'USA',
                                    'addressType': 'RESIDENTIAL'
                                }
                            },
                            'orderLines': {
                                'orderLine': [{
                                    'lineNumber': '1',
                                    'item': {
                                        'productName': 'Little Girls Tutu 3-Layer Ballerina Silver',
                                        'sku': '1702-007'
                                    },
                                    'charges': {
                                        'charge': [{
                                                'chargeType': 'PRODUCT',
                                                'chargeName': 'ItemPrice',
                                                'chargeAmount': {
                                                    'currency': 'USD',
                                                    'amount': 3.99
                                                },
                                                'tax': {
                                                    'taxName': 'Tax1',
                                                    'taxAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.28
                                                    }
                                                }
                                            },
                                            {
                                                'chargeType': 'SHIPPING',
                                                'chargeName': 'Shipping',
                                                'chargeAmount': {
                                                    'currency': 'USD',
                                                    'amount': 2.99
                                                },
                                                'tax': {
                                                    'taxName': 'Tax1',
                                                    'taxAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.21
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    'orderLineQuantity': {
                                        'unitOfMeasurement': 'EACH',
                                        'amount': '1'
                                    },
                                    'statusDate': 1563865276000,
                                    'orderLineStatuses': {
                                        'orderLineStatus': [{
                                            'status': 'Acknowledged',
                                            'statusQuantity': {
                                                'unitOfMeasurement': 'EACH',
                                                'amount': '1'
                                            },
                                            'cancellationReason': None,
                                            'trackingInfo': None
                                        }]
                                    },
                                    'refund': None,
                                    'fulfillment': {
                                        'fulfillmentOption': 'S2H',
                                        'shipMethod': 'STANDARD',
                                        'storeId': None,
                                        'pickUpDateTime': 1564599600000,
                                        'pickUpBy': None
                                    }
                                }]
                            }
                        },
                        {
                            'purchaseOrderId': '1795749953091',
                            'customerOrderId': '4751966824128',
                            'customerEmailId': 'C69B6547505944D7851FC44EA9429DD3@relay.walmart.com',
                            'orderDate': 1563853788000,
                            'shippingInfo': {
                                'phone': '6186045881',
                                'estimatedDeliveryDate': 1565031600000,
                                'estimatedShipDate': 1564459200000,
                                'methodCode': 'Standard',
                                'postalAddress': {
                                    'name': 'KARIE Sweitzer',
                                    'address1': '5020 N ILLINOIS ST',
                                    'address2': None,
                                    'city': 'Fairview Heights',
                                    'state': 'IL',
                                    'postalCode': '62208',
                                    'country': 'USA',
                                    'addressType': 'OFFICE'
                                }
                            },
                            'orderLines': {
                                'orderLine': [{
                                        'lineNumber': '1',
                                        'item': {
                                            'productName': '2.25" Apple Green Grosgrain Ribbon Solid 5 yard',
                                            'sku': '101010-321405550'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 2.45
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.2
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 1.26
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.1
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563865278000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    },
                                    {
                                        'lineNumber': '2',
                                        'item': {
                                            'productName': '2.25" Light Turquoise Grosgrain Ribbon Solid 5 yard',
                                            'sku': '101010-321405319'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 2.45
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.21
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 1.25
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.1
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563865278000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    },
                                    {
                                        'lineNumber': '3',
                                        'item': {
                                            'productName': '2.25" Purple Grosgrain Ribbon Solid 5 yard',
                                            'sku': '101010-321405465'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 2.45
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.2
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 1.25
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.1
                                                        }
                                                    }
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563865278000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': None
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            'purchaseOrderId': '4792049857354',
                            'customerOrderId': '4741965197147',
                            'customerEmailId': '4955FD2EADCD458DAEE9006B0A6E7E6A@relay.walmart.com',
                            'orderDate': 1563830916000,
                            'shippingInfo': {
                                'phone': '6783990955',
                                'estimatedDeliveryDate': 1565031600000,
                                'estimatedShipDate': 1564459200000,
                                'methodCode': 'Standard',
                                'postalAddress': {
                                    'name': 'Sandra Quizza Garcia',
                                    'address1': '2979 Lake Colony Dr NW, Norcross',
                                    'address2': 'Apartament #16',
                                    'city': 'Peachtree Corners',
                                    'state': 'GA',
                                    'postalCode': '30071',
                                    'country': 'USA',
                                    'addressType': 'RESIDENTIAL'
                                }
                            },
                            'orderLines': {
                                'orderLine': [{
                                    'lineNumber': '2',
                                    'item': {
                                        'productName': 'Little Girls Tutu 3-Layer Ballerina Turquoise',
                                        'sku': '1702-340'
                                    },
                                    'charges': {
                                        'charge': [{
                                                'chargeType': 'PRODUCT',
                                                'chargeName': 'ItemPrice',
                                                'chargeAmount': {
                                                    'currency': 'USD',
                                                    'amount': 3.99
                                                },
                                                'tax': {
                                                    'taxName': 'Tax1',
                                                    'taxAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.24
                                                    }
                                                }
                                            },
                                            {
                                                'chargeType': 'SHIPPING',
                                                'chargeName': 'Shipping',
                                                'chargeAmount': {
                                                    'currency': 'USD',
                                                    'amount': 2.99
                                                },
                                                'tax': {
                                                    'taxName': 'Tax1',
                                                    'taxAmount': {
                                                        'currency': 'USD',
                                                        'amount': 0.18
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    'orderLineQuantity': {
                                        'unitOfMeasurement': 'EACH',
                                        'amount': '1'
                                    },
                                    'statusDate': 1563836072000,
                                    'orderLineStatuses': {
                                        'orderLineStatus': [{
                                            'status': 'Acknowledged',
                                            'statusQuantity': {
                                                'unitOfMeasurement': 'EACH',
                                                'amount': '1'
                                            },
                                            'cancellationReason': None,
                                            'trackingInfo': None
                                        }]
                                    },
                                    'refund': None,
                                    'fulfillment': {
                                        'fulfillmentOption': 'S2H',
                                        'shipMethod': 'STANDARD',
                                        'storeId': None,
                                        'pickUpDateTime': 1564599600000,
                                        'pickUpBy': 'Sandra Quizza Garcia'
                                    }
                                }]
                            }
                        },
                        {
                            'purchaseOrderId': '3795739830204',
                            'customerOrderId': '4741966904458',
                            'customerEmailId': '1AD83B3162AD4B57ADC8F180FBCE1D0F@relay.walmart.com',
                            'orderDate': 1563830290000,
                            'shippingInfo': {
                                'phone': '7574393272',
                                'estimatedDeliveryDate': 1565031600000,
                                'estimatedShipDate': 1564459200000,
                                'methodCode': 'Standard',
                                'postalAddress': {
                                    'name': 'Laura Elliott',
                                    'address1': '1929 Orangewood Road',
                                    'address2': None,
                                    'city': 'Chesapeake',
                                    'state': 'VA',
                                    'postalCode': '23323',
                                    'country': 'USA',
                                    'addressType': 'RESIDENTIAL'
                                }
                            },
                            'orderLines': {
                                'orderLine': [{
                                        'lineNumber': '6',
                                        'item': {
                                            'productName': '3" Fuchsia Grosgrain Ribbon Solid 3 yard',
                                            'sku': '101010-3303187'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 2.5
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.15
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 1.8
                                                    },
                                                    'tax': None
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563836074000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': 'Laura Elliott'
                                        }
                                    },
                                    {
                                        'lineNumber': '9',
                                        'item': {
                                            'productName': '3" Fuchsia Grosgrain Ribbon Solid 3 yard',
                                            'sku': '101010-3303187'
                                        },
                                        'charges': {
                                            'charge': [{
                                                    'chargeType': 'PRODUCT',
                                                    'chargeName': 'ItemPrice',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 2.5
                                                    },
                                                    'tax': {
                                                        'taxName': 'Tax1',
                                                        'taxAmount': {
                                                            'currency': 'USD',
                                                            'amount': 0.15
                                                        }
                                                    }
                                                },
                                                {
                                                    'chargeType': 'SHIPPING',
                                                    'chargeName': 'Shipping',
                                                    'chargeAmount': {
                                                        'currency': 'USD',
                                                        'amount': 1.79
                                                    },
                                                    'tax': None
                                                }
                                            ]
                                        },
                                        'orderLineQuantity': {
                                            'unitOfMeasurement': 'EACH',
                                            'amount': '1'
                                        },
                                        'statusDate': 1563836074000,
                                        'orderLineStatuses': {
                                            'orderLineStatus': [{
                                                'status': 'Acknowledged',
                                                'statusQuantity': {
                                                    'unitOfMeasurement': 'EACH',
                                                    'amount': '1'
                                                },
                                                'cancellationReason': None,
                                                'trackingInfo': None
                                            }]
                                        },
                                        'refund': None,
                                        'fulfillment': {
                                            'fulfillmentOption': 'S2H',
                                            'shipMethod': 'STANDARD',
                                            'storeId': None,
                                            'pickUpDateTime': 1564599600000,
                                            'pickUpBy': 'Laura Elliott'
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    elif resource == "items":
        return {
            'ItemResponse': [{
                'mart': 'WALMART_US',
                'sku': '101013-21550015340',
                'wpid': '0REAG121OH3P',
                'upc': '635510505068',
                'gtin': '00635510505068',
                'productName': '1.5" Large Turquoise Dot Grosgrain Ribbon 50yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 29.62
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-43805580',
                'wpid': '0RJG1KW2E37W',
                'upc': '635510489702',
                'gtin': '00635510489702',
                'productName': '3/8" Grosgrain Ribbon Solid 580 Emerald 5yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 0.89
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '1012-8303550',
                'wpid': '0RJXCK8SQ473',
                'upc': '635510510468',
                'gtin': '00635510510468',
                'productName': '3" Apple Green Double Faced Satin Ribbon 3 yard',
                'shelf': '["UNNAV"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 3.5
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-61550343',
                'wpid': '0RLO0K8LGD1U',
                'upc': '635510496908',
                'gtin': '00635510496908',
                'productName': '1.5" Grosgrain Ribbon Solid 343 Tornado Blue 50yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 13.54
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-57805012',
                'wpid': '0RN8TX8OZB5K',
                'upc': '635510492108',
                'gtin': '00635510492108',
                'productName': '7/8" Grosgrain Ribbon Solid 012 Silver 5yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Graduation Party Supplies","Graduation Decorations","Graduation Balloon Accessories"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 1.15
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101610-615100159',
                'wpid': '0RNLB1V4LVVS',
                'upc': '635510514220',
                'gtin': '00635510514220',
                'productName': '1.5" Grosgrain Ribbon Solid 159 Passion Fruit 100yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 23.95
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '1009-51503462',
                'wpid': '0RNV1W9F1F54',
                'upc': '635510482611',
                'gtin': '00635510482611',
                'productName': '1.5" Lavender Glitter Ribbon 3yd',
                'shelf': '["UNNAV"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 5.39
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-578W05587',
                'wpid': '0ROYJP2R8I1N',
                'upc': '635510494515',
                'gtin': '00635510494515',
                'productName': '7/8" Grosgrain Ribbon White Dots 587 Forest Green 5 Yard',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 3.25
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101610-33100460',
                'wpid': '0RP0E74L2AF5',
                'upc': '635510512561',
                'gtin': '00635510512561',
                'productName': '3" Lavender Grosgrain Ribbon Solid 100 yard',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 56.49
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '1012-722525660',
                'wpid': '0RRCI3UAV1W8',
                'upc': '635510509905',
                'gtin': '00635510509905',
                'productName': '2.25" Yellow Gold Double Face Satin Ribbon 25 yard Reel',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 13.59
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-61505352',
                'wpid': '0RWDDY5IJOUQ',
                'upc': '635510495413',
                'gtin': '00635510495413',
                'productName': '1.5" Grosgrain Ribbon Solid 352 Royal Blue 5yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 1.69
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '1012-8303463',
                'wpid': '0RWLG8N05H39',
                'upc': '635510510420',
                'gtin': '00635510510420',
                'productName': '3" Grape Double Faced Satin Ribbon 3 yard',
                'shelf': '["UNNAV"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 3.5
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101610-578100580',
                'wpid': '0RYUK6TQ09UQ',
                'upc': '635510513827',
                'gtin': '00635510513827',
                'productName': '7/8" Grosgrain Ribbon Solid 580 Emerald 100yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 13.95
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101610-3214100835',
                'wpid': '0RZPEXN3XP8V',
                'upc': '635510512363',
                'gtin': '00635510512363',
                'productName': '2.25" Tan Grosgrain Ribbon Solid 100 yard',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 35.95
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-321405460',
                'wpid': '0S3YUTERLFTM',
                'upc': '635510486855',
                'gtin': '00635510486855',
                'productName': '2.25" Lavender Grosgrain Ribbon Solid 5 yard',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 2.45
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101013-21525032030',
                'wpid': '0S6WZXI0KTXP',
                'upc': '635510516521',
                'gtin': '00635510516521',
                'productName': '1.5" Black Damask Grosgrain Ribbon 25yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 15.67
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101013-21505045OM',
                'wpid': '0S7CUGHJW3F3',
                'upc': '635510522799',
                'gtin': '00635510522799',
                'productName': '1.5" Ombre Rainbow Cheer Text Grosgrain Ribbon 5yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 5.29
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-61505123',
                'wpid': '0SBAGTW9UBXK',
                'upc': '635510495093',
                'gtin': '00635510495093',
                'productName': '1.5" Grosgrain Ribbon Solid 123 Pearl Pink 5yd',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 1.69
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101009-17810156030',
                'wpid': '0SIO1G8K4CCH',
                'upc': '635510483373',
                'gtin': '00635510483373',
                'productName': '7/8" Hot Pink / Black Moonstitch Grosgrain Ribbon 10yd',
                'shelf': '["UNNAV"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 5.25
                },
                'publishedStatus': 'PUBLISHED'
            },
            {
                'mart': 'WALMART_US',
                'sku': '101010-25805524',
                'wpid': '0SJ5B6GAPLJN',
                'upc': '635510485759',
                'gtin': '00635510485759',
                'productName': '5/8" Lime Juice Grosgrain Ribbon Solid 5 yard reel (16mm) HairBow Center',
                'shelf': '["Home Page","Party & Occasions","Party Supplies","Gift Wrap & Supplies"]',
                'productType': 'Ribbons & Bows',
                'price': {
                    'currency': 'USD',
                    'amount': 1.99
                },
                'publishedStatus': 'PUBLISHED'
            }],
            'totalItems': 3111,
            'nextCursor': 'AoE/GjBTSjVCNkdBUExKTjBTRUxMRVJfT0ZGRVJERTAwMDdENzMxQ0Q0RTU5ODcxMjkzMDZBQjE5OEVFMw=='
        }
    return [{}]
