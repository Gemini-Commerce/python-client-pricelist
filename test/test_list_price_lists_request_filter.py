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

from pricelist.models.list_price_lists_request_filter import ListPriceListsRequestFilter

class TestListPriceListsRequestFilter(unittest.TestCase):
    """ListPriceListsRequestFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListPriceListsRequestFilter:
        """Test ListPriceListsRequestFilter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListPriceListsRequestFilter`
        """
        model = ListPriceListsRequestFilter()
        if include_optional:
            return ListPriceListsRequestFilter(
                code = '',
                name = '',
                description = '',
                is_active = True,
                is_default = True,
                currency_filter = pricelist.models.pricelist_currency_filter.pricelistCurrencyFilter(
                    currencies = [
                        'XXX'
                        ], 
                    condition = 'IN', ),
                vat_included = True,
                delivered_duty_paid = True,
                segments_filter = pricelist.models.pricelist_segment_filter.pricelistSegmentFilter(
                    segments = [
                        ''
                        ], 
                    condition = 'IN', ),
                markets_filter = pricelist.models.pricelist_market_filter.pricelistMarketFilter(
                    markets = [
                        ''
                        ], 
                    condition = 'IN', ),
                channels_filter = pricelist.models.pricelist_channel_filter.pricelistChannelFilter(
                    channels = [
                        ''
                        ], 
                    condition = 'IN', ),
                type_filter = pricelist.models.pricelist_price_list_type_filter.pricelistPriceListTypeFilter(
                    pricelist_types = [
                        'UNKNOWN'
                        ], 
                    condition = 'IN', ),
                is_system = True
            )
        else:
            return ListPriceListsRequestFilter(
        )
        """

    def testListPriceListsRequestFilter(self):
        """Test ListPriceListsRequestFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
