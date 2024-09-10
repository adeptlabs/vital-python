# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingElectrocardiogramVoltageTimeseries(pydantic.BaseModel):
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
    The lead of the measurement.
    """

    unit: str = pydantic.Field()
    """
    Measured in mV.
    """

    timestamp: str = pydantic.Field()
    """
    The timestamp of the measurement.
    """

    value: float = pydantic.Field()
    """
    The value of the measurement.
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
