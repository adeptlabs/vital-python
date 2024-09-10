# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .source_auth_type import SourceAuthType
from .source_type import SourceType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Source(pydantic.BaseModel):
    name: str
    slug: str
    description: str
    logo: str
    group: typing.Optional[str] = None
    oauth_url: typing.Optional[str] = None
    auth_type: typing.Optional[SourceAuthType] = None
    source_type: typing.Optional[SourceType] = None
    is_active: typing.Optional[bool] = None
    backfill_num_days: typing.Optional[int] = None
    id: int

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
