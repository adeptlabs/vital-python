# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SleepColumnExprSleep(str, enum.Enum):
    SESSION_START = "session_start"
    SESSION_END = "session_end"
    STATE = "state"
    TYPE = "type"
    DURATION_SECOND = "duration_second"
    STAGE_ASLEEP_SECOND = "stage_asleep_second"
    STAGE_AWAKE_SECOND = "stage_awake_second"
    STAGE_LIGHT_SECOND = "stage_light_second"
    STAGE_REM_SECOND = "stage_rem_second"
    STAGE_DEEP_SECOND = "stage_deep_second"
    STAGE_UNKNOWN_SECOND = "stage_unknown_second"
    LATENCY_SECOND = "latency_second"
    HEART_RATE_MINIMUM = "heart_rate_minimum"
    HEART_RATE_MEAN = "heart_rate_mean"
    HEART_RATE_MAXIMUM = "heart_rate_maximum"
    HEART_RATE_DIP = "heart_rate_dip"
    EFFICIENCY = "efficiency"
    HRV_MEAN_RMSSD = "hrv_mean_rmssd"
    HRV_MEAN_SDNN = "hrv_mean_sdnn"
    SKIN_TEMPERATURE_DELTA = "skin_temperature_delta"
    RESPIRATORY_RATE = "respiratory_rate"
    SCORE = "score"
    SOURCE_TYPE = "source_type"
    SOURCE_PROVIDER = "source_provider"
    SOURCE_APP_ID = "source_app_id"

    def visit(
        self,
        session_start: typing.Callable[[], T_Result],
        session_end: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        type: typing.Callable[[], T_Result],
        duration_second: typing.Callable[[], T_Result],
        stage_asleep_second: typing.Callable[[], T_Result],
        stage_awake_second: typing.Callable[[], T_Result],
        stage_light_second: typing.Callable[[], T_Result],
        stage_rem_second: typing.Callable[[], T_Result],
        stage_deep_second: typing.Callable[[], T_Result],
        stage_unknown_second: typing.Callable[[], T_Result],
        latency_second: typing.Callable[[], T_Result],
        heart_rate_minimum: typing.Callable[[], T_Result],
        heart_rate_mean: typing.Callable[[], T_Result],
        heart_rate_maximum: typing.Callable[[], T_Result],
        heart_rate_dip: typing.Callable[[], T_Result],
        efficiency: typing.Callable[[], T_Result],
        hrv_mean_rmssd: typing.Callable[[], T_Result],
        hrv_mean_sdnn: typing.Callable[[], T_Result],
        skin_temperature_delta: typing.Callable[[], T_Result],
        respiratory_rate: typing.Callable[[], T_Result],
        score: typing.Callable[[], T_Result],
        source_type: typing.Callable[[], T_Result],
        source_provider: typing.Callable[[], T_Result],
        source_app_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SleepColumnExprSleep.SESSION_START:
            return session_start()
        if self is SleepColumnExprSleep.SESSION_END:
            return session_end()
        if self is SleepColumnExprSleep.STATE:
            return state()
        if self is SleepColumnExprSleep.TYPE:
            return type()
        if self is SleepColumnExprSleep.DURATION_SECOND:
            return duration_second()
        if self is SleepColumnExprSleep.STAGE_ASLEEP_SECOND:
            return stage_asleep_second()
        if self is SleepColumnExprSleep.STAGE_AWAKE_SECOND:
            return stage_awake_second()
        if self is SleepColumnExprSleep.STAGE_LIGHT_SECOND:
            return stage_light_second()
        if self is SleepColumnExprSleep.STAGE_REM_SECOND:
            return stage_rem_second()
        if self is SleepColumnExprSleep.STAGE_DEEP_SECOND:
            return stage_deep_second()
        if self is SleepColumnExprSleep.STAGE_UNKNOWN_SECOND:
            return stage_unknown_second()
        if self is SleepColumnExprSleep.LATENCY_SECOND:
            return latency_second()
        if self is SleepColumnExprSleep.HEART_RATE_MINIMUM:
            return heart_rate_minimum()
        if self is SleepColumnExprSleep.HEART_RATE_MEAN:
            return heart_rate_mean()
        if self is SleepColumnExprSleep.HEART_RATE_MAXIMUM:
            return heart_rate_maximum()
        if self is SleepColumnExprSleep.HEART_RATE_DIP:
            return heart_rate_dip()
        if self is SleepColumnExprSleep.EFFICIENCY:
            return efficiency()
        if self is SleepColumnExprSleep.HRV_MEAN_RMSSD:
            return hrv_mean_rmssd()
        if self is SleepColumnExprSleep.HRV_MEAN_SDNN:
            return hrv_mean_sdnn()
        if self is SleepColumnExprSleep.SKIN_TEMPERATURE_DELTA:
            return skin_temperature_delta()
        if self is SleepColumnExprSleep.RESPIRATORY_RATE:
            return respiratory_rate()
        if self is SleepColumnExprSleep.SCORE:
            return score()
        if self is SleepColumnExprSleep.SOURCE_TYPE:
            return source_type()
        if self is SleepColumnExprSleep.SOURCE_PROVIDER:
            return source_provider()
        if self is SleepColumnExprSleep.SOURCE_APP_ID:
            return source_app_id()
