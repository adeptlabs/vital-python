# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .client_facing_heart_rate import ClientFacingHeartRate
from .client_facing_source import ClientFacingSource

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingActivity(pydantic.BaseModel):
    user_id: str = pydantic.Field(
        description="User id returned by vital create user request. This id should be stored in your database against the user and used for all interactions with the vital api."
    )
    id: str
    date: str = pydantic.Field(
        description="Date of the specified record, formatted as ISO8601 datetime string in UTC 00:00. Deprecated in favour of calendar_date."
    )
    calendar_date: str = pydantic.Field(description="Date of the summary in the YYYY-mm-dd format.")
    calories_total: typing.Optional[float]
    calories_active: typing.Optional[float]
    steps: typing.Optional[int]
    daily_movement: typing.Optional[float]
    distance: typing.Optional[float]
    low: typing.Optional[float]
    medium: typing.Optional[float]
    high: typing.Optional[float]
    source: ClientFacingSource = pydantic.Field(description="Source the data has come from.")
    floors_climbed: typing.Optional[int]
    time_zone: typing.Optional[str]
    timezone_offset: typing.Optional[int]
    heart_rate: typing.Optional[ClientFacingHeartRate]

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
