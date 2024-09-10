# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .fats import Fats

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Macros(pydantic.BaseModel):
    carbs: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of carbohydrates in grams (g)
    """

    protein: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of protein in grams (g)
    """

    fats: typing.Optional[Fats] = pydantic.Field(default=None)
    """
    Details of fat content
    """

    alcohol: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of alcohol in grams (g)
    """

    water: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of water in grams (g)
    """

    fibre: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of dietary fiber in grams (g)
    """

    sugar: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of sugar in grams (g)
    """

    cholesterol: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of cholesterol in grams (g)
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
