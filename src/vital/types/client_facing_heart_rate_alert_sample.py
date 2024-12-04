# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .client_facing_heart_rate_alert_sample_type import ClientFacingHeartRateAlertSampleType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientFacingHeartRateAlertSample(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated
    """

    timezone_offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time zone UTC offset in seconds. Positive offset indicates east of UTC; negative offset indicates west of UTC; and null indicates the time zone information is unavailable at source.
    """

    type: ClientFacingHeartRateAlertSampleType
    unit: typing.Literal["count"] = "count"
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

    value: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
