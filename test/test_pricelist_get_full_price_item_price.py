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

from pricelist.models.pricelist_get_full_price_item_price import PricelistGetFullPriceItemPrice

class TestPricelistGetFullPriceItemPrice(unittest.TestCase):
    """PricelistGetFullPriceItemPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistGetFullPriceItemPrice:
        """Test PricelistGetFullPriceItemPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistGetFullPriceItemPrice`
        """
        model = PricelistGetFullPriceItemPrice()
        if include_optional:
            return PricelistGetFullPriceItemPrice(
                price = pricelist.models.pricelist_money.pricelistMoney(
                    units = '', 
                    micros = 56, ),
                is_enabled = True,
                start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order = 56,
                base_price = pricelist.models.pricelist_money.pricelistMoney(
                    units = '', 
                    micros = 56, )
            )
        else:
            return PricelistGetFullPriceItemPrice(
        )
        """

    def testPricelistGetFullPriceItemPrice(self):
        """Test PricelistGetFullPriceItemPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()