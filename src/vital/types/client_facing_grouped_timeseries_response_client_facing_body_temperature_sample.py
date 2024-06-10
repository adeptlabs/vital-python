# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_timeseries_group_client_facing_body_temperature_sample import (
    ClientFacingTimeseriesGroupClientFacingBodyTemperatureSample,
)

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingGroupedTimeseriesResponseClientFacingBodyTemperatureSample(pydantic.BaseModel):
    groups: typing.Dict[
        str, typing.List[ClientFacingTimeseriesGroupClientFacingBodyTemperatureSample]
    ] = pydantic.Field(description="For each matching provider or lab, a list of grouped timeseries values.")
    next: typing.Optional[str]

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
