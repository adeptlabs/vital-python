# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .ao_e import AoE
from .client_facing_result import ClientFacingResult
from .marker_type import MarkerType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingMarkerComplete(pydantic.BaseModel):
    id: int
    name: str
    slug: str
    description: typing.Optional[str]
    lab_id: typing.Optional[int]
    provider_id: typing.Optional[str]
    type: typing.Optional[MarkerType]
    unit: typing.Optional[str]
    price: typing.Optional[str]
    aoe: typing.Optional[AoE]
    expected_results: typing.List[ClientFacingResult]

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
