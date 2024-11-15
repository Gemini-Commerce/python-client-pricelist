# coding: utf-8

"""
    PriceList Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pricelist.models.pricelist_channel_filter import PricelistChannelFilter
from pricelist.models.pricelist_currency_filter import PricelistCurrencyFilter
from pricelist.models.pricelist_market_filter import PricelistMarketFilter
from pricelist.models.pricelist_price_list_type_filter import PricelistPriceListTypeFilter
from pricelist.models.pricelist_segment_filter import PricelistSegmentFilter
from typing import Optional, Set
from typing_extensions import Self

class ListPriceListsRequestFilter(BaseModel):
    """
    ListPriceListsRequestFilter
    """ # noqa: E501
    code: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    is_active: Optional[StrictBool] = Field(default=None, alias="isActive")
    is_default: Optional[StrictBool] = Field(default=None, alias="isDefault")
    currency_filter: Optional[PricelistCurrencyFilter] = Field(default=None, alias="currencyFilter")
    vat_included: Optional[StrictBool] = Field(default=None, alias="vatIncluded")
    delivered_duty_paid: Optional[StrictBool] = Field(default=None, alias="deliveredDutyPaid")
    segments_filter: Optional[PricelistSegmentFilter] = Field(default=None, alias="segmentsFilter")
    markets_filter: Optional[PricelistMarketFilter] = Field(default=None, alias="marketsFilter")
    channels_filter: Optional[PricelistChannelFilter] = Field(default=None, alias="channelsFilter")
    type_filter: Optional[PricelistPriceListTypeFilter] = Field(default=None, alias="typeFilter")
    is_system: Optional[StrictBool] = Field(default=None, alias="isSystem")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["code", "name", "description", "isActive", "isDefault", "currencyFilter", "vatIncluded", "deliveredDutyPaid", "segmentsFilter", "marketsFilter", "channelsFilter", "typeFilter", "isSystem"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListPriceListsRequestFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of currency_filter
        if self.currency_filter:
            _dict['currencyFilter'] = self.currency_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of segments_filter
        if self.segments_filter:
            _dict['segmentsFilter'] = self.segments_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of markets_filter
        if self.markets_filter:
            _dict['marketsFilter'] = self.markets_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channels_filter
        if self.channels_filter:
            _dict['channelsFilter'] = self.channels_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type_filter
        if self.type_filter:
            _dict['typeFilter'] = self.type_filter.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListPriceListsRequestFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "isActive": obj.get("isActive"),
            "isDefault": obj.get("isDefault"),
            "currencyFilter": PricelistCurrencyFilter.from_dict(obj["currencyFilter"]) if obj.get("currencyFilter") is not None else None,
            "vatIncluded": obj.get("vatIncluded"),
            "deliveredDutyPaid": obj.get("deliveredDutyPaid"),
            "segmentsFilter": PricelistSegmentFilter.from_dict(obj["segmentsFilter"]) if obj.get("segmentsFilter") is not None else None,
            "marketsFilter": PricelistMarketFilter.from_dict(obj["marketsFilter"]) if obj.get("marketsFilter") is not None else None,
            "channelsFilter": PricelistChannelFilter.from_dict(obj["channelsFilter"]) if obj.get("channelsFilter") is not None else None,
            "typeFilter": PricelistPriceListTypeFilter.from_dict(obj["typeFilter"]) if obj.get("typeFilter") is not None else None,
            "isSystem": obj.get("isSystem")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


