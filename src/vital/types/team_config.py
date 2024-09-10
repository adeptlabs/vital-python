# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .event_destination_preferences import EventDestinationPreferences
from .libre_config import LibreConfig

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TeamConfig(pydantic.BaseModel):
    libreview: LibreConfig
    texts_enabled: typing.Optional[bool] = None
    push_historical_data: typing.Optional[bool] = None
    provider_raw_data: typing.Optional[bool] = None
    reject_duplicate_connection: typing.Optional[bool] = None
    sdk_per_device_activity_timeseries: typing.Optional[bool] = None
    eds_preferences: typing.Optional[EventDestinationPreferences] = None
    event_type_prefixes: typing.Optional[typing.List[str]] = None

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
