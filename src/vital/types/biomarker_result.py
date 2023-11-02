# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .result_type import ResultType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BiomarkerResult(pydantic.BaseModel):
    """
    Represent the schema for an individual biomarker result.
    """

    name: str
    slug: typing.Optional[str]
    value: float
    result: str
    type: ResultType
    unit: typing.Optional[str]
    timestamp: typing.Optional[dt.datetime]
    notes: typing.Optional[str]
    min_range_value: typing.Optional[float]
    max_range_value: typing.Optional[float]
    is_above_max_range: typing.Optional[bool]
    is_below_min_range: typing.Optional[bool]
    interpretation: typing.Optional[str]
    loinc: typing.Optional[str]
    loinc_slug: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
