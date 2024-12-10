# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .aggregation_result import AggregationResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AggregationResponse(UniversalBaseModel):
    results: typing.List[AggregationResult]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
