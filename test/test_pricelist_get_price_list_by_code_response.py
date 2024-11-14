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

from pricelist.models.pricelist_get_price_list_by_code_response import PricelistGetPriceListByCodeResponse

class TestPricelistGetPriceListByCodeResponse(unittest.TestCase):
    """PricelistGetPriceListByCodeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricelistGetPriceListByCodeResponse:
        """Test PricelistGetPriceListByCodeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricelistGetPriceListByCodeResponse`
        """
        model = PricelistGetPriceListByCodeResponse()
        if include_optional:
            return PricelistGetPriceListByCodeResponse(
                id = '',
                grn = '',
                code = '',
                name = '',
                description = '',
                is_active = True,
                is_default = True,
                currency = 'XXX',
                vat_included = True,
                delivered_duty_paid = True,
                segments = [
                    ''
                    ],
                markets = [
                    ''
                    ],
                channels = [
                    ''
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = 'UNKNOWN',
                is_system = True
            )
        else:
            return PricelistGetPriceListByCodeResponse(
        )
        """

    def testPricelistGetPriceListByCodeResponse(self):
        """Test PricelistGetPriceListByCodeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
