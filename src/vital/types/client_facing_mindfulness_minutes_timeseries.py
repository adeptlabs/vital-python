# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingMindfulnessMinutesTimeseries(pydantic.BaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reading type of the measurement. This is applicable only to Cholesterol, IGG, IGE and InsulinInjection.
    """

    unit: str = pydantic.Field()
    """
    Measured in minutes.
    """

    timestamp: str = pydantic.Field()
    """
    Depracated. The start time (inclusive) of the interval.
    """

    start: str = pydantic.Field()
    """
    The start time (inclusive) of the interval.
    """

    end: str = pydantic.Field()
    """
    The end time (exclusive) of the interval.
    """

    value: float = pydantic.Field()
    """
    Number of minutes spent in a mindful state.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
