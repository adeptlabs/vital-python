# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .resource_availability import ResourceAvailability

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ClientFacingProviderWithStatus(pydantic.BaseModel):
    name: str = pydantic.Field()
    """
    Name of source of information
    """

    slug: str = pydantic.Field()
    """
    Slug for designated source
    """

    logo: str = pydantic.Field()
    """
    URL for source logo
    """

    status: str = pydantic.Field()
    """
    Status of source, either error or connected
    """

    resource_availability: typing.Dict[str, ResourceAvailability]

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
