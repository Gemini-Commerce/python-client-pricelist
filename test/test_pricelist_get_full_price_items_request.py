# coding: utf-8

"""
    PriceList Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pricelist.models.pricelist_get_full_price_items_request import PricelistGetFullPriceItemsRequest

class TestPricelistGetFullPriceItemsRequest(unittest.TestCase):
    """PricelistGetFullPriceItemsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistGetFullPriceItemsRequest:
        """Test PricelistGetFullPriceItemsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistGetFullPriceItemsRequest`
        """
        model = PricelistGetFullPriceItemsRequest()
        if include_optional:
            return PricelistGetFullPriceItemsRequest(
                tenant_id = '',
                pricelist_id = '',
                items_grn = [
                    ''
                    ]
            )
        else:
            return PricelistGetFullPriceItemsRequest(
        )
        """

    def testPricelistGetFullPriceItemsRequest(self):
        """Test PricelistGetFullPriceItemsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
