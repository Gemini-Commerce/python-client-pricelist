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

from pricelist.models.pricelist_set_price_list_items_request import PricelistSetPriceListItemsRequest

class TestPricelistSetPriceListItemsRequest(unittest.TestCase):
    """PricelistSetPriceListItemsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistSetPriceListItemsRequest:
        """Test PricelistSetPriceListItemsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistSetPriceListItemsRequest`
        """
        model = PricelistSetPriceListItemsRequest()
        if include_optional:
            return PricelistSetPriceListItemsRequest(
                tenant_id = '',
                id = '',
                items = [
                    pricelist.models.pricelist_set_price_list_item.pricelistSetPriceListItem(
                        item_grn = '', 
                        base_price = pricelist.models.pricelist_money.pricelistMoney(
                            units = '', 
                            micros = 56, ), 
                        price_items = [
                            pricelist.models.pricelist_set_price_list_item_price.pricelistSetPriceListItemPrice(
                                price = pricelist.models.pricelist_money.pricelistMoney(
                                    units = '', 
                                    micros = 56, ), 
                                is_enabled = True, 
                                start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                order = 56, )
                            ], 
                        has_tier_prices = True, )
                    ]
            )
        else:
            return PricelistSetPriceListItemsRequest(
        )
        """

    def testPricelistSetPriceListItemsRequest(self):
        """Test PricelistSetPriceListItemsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()