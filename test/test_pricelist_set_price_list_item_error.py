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

from pricelist.models.pricelist_set_price_list_item_error import PricelistSetPriceListItemError

class TestPricelistSetPriceListItemError(unittest.TestCase):
    """PricelistSetPriceListItemError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistSetPriceListItemError:
        """Test PricelistSetPriceListItemError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistSetPriceListItemError`
        """
        model = PricelistSetPriceListItemError()
        if include_optional:
            return PricelistSetPriceListItemError(
                item_grn = '',
                code = '',
                description = ''
            )
        else:
            return PricelistSetPriceListItemError(
        )
        """

    def testPricelistSetPriceListItemError(self):
        """Test PricelistSetPriceListItemError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
