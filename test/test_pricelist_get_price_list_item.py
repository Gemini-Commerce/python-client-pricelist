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

from pricelist.models.pricelist_get_price_list_item import PricelistGetPriceListItem

class TestPricelistGetPriceListItem(unittest.TestCase):
    """PricelistGetPriceListItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistGetPriceListItem:
        """Test PricelistGetPriceListItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistGetPriceListItem`
        """
        model = PricelistGetPriceListItem()
        if include_optional:
            return PricelistGetPriceListItem(
                id = '',
                grn = '',
                item_grn = '',
                price = pricelist.models.pricelist_money.pricelistMoney(
                    units = '', 
                    micros = 56, ),
                double_format_price = 1.337,
                end_date_price = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                base_price = pricelist.models.pricelist_money.pricelistMoney(
                    units = '', 
                    micros = 56, ),
                double_format_base_price = 1.337,
                currency = 'XXX',
                has_tier_prices = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PricelistGetPriceListItem(
        )
        """

    def testPricelistGetPriceListItem(self):
        """Test PricelistGetPriceListItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
