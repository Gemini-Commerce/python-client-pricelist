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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pricelist.models.pricelist_currency import PricelistCurrency
from pricelist.models.pricelist_money import PricelistMoney
from typing import Optional, Set
from typing_extensions import Self

class PricelistGetPriceItem(BaseModel):
    """
    PricelistGetPriceItem
    """ # noqa: E501
    item_grn: Optional[StrictStr] = Field(default=None, alias="itemGrn")
    price: Optional[PricelistMoney] = None
    double_format_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="doubleFormatPrice")
    end_date_price: Optional[datetime] = Field(default=None, alias="endDatePrice")
    base_price: Optional[PricelistMoney] = Field(default=None, alias="basePrice")
    double_format_base_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="doubleFormatBasePrice")
    currency: Optional[PricelistCurrency] = PricelistCurrency.XXX
    has_tier_prices: Optional[StrictBool] = Field(default=None, alias="hasTierPrices")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["itemGrn", "price", "doubleFormatPrice", "endDatePrice", "basePrice", "doubleFormatBasePrice", "currency", "hasTierPrices", "createdAt", "updatedAt"]

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
        """Create an instance of PricelistGetPriceItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of base_price
        if self.base_price:
            _dict['basePrice'] = self.base_price.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PricelistGetPriceItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemGrn": obj.get("itemGrn"),
            "price": PricelistMoney.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "doubleFormatPrice": obj.get("doubleFormatPrice"),
            "endDatePrice": obj.get("endDatePrice"),
            "basePrice": PricelistMoney.from_dict(obj["basePrice"]) if obj.get("basePrice") is not None else None,
            "doubleFormatBasePrice": obj.get("doubleFormatBasePrice"),
            "currency": obj.get("currency") if obj.get("currency") is not None else PricelistCurrency.XXX,
            "hasTierPrices": obj.get("hasTierPrices"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


