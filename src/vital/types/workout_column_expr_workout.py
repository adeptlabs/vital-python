# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WorkoutColumnExprWorkout(str, enum.Enum):
    SESSION_START = "session_start"
    SESSION_END = "session_end"
    TITLE = "title"
    SPORT_NAME = "sport_name"
    SPORT_SLUG = "sport_slug"
    DURATION_ACTIVE_SECOND = "duration_active_second"
    HEART_RATE_MEAN = "heart_rate_mean"
    HEART_RATE_MINIMUM = "heart_rate_minimum"
    HEART_RATE_MAXIMUM = "heart_rate_maximum"
    HEART_RATE_ZONE_1 = "heart_rate_zone_1"
    HEART_RATE_ZONE_2 = "heart_rate_zone_2"
    HEART_RATE_ZONE_3 = "heart_rate_zone_3"
    HEART_RATE_ZONE_4 = "heart_rate_zone_4"
    HEART_RATE_ZONE_5 = "heart_rate_zone_5"
    HEART_RATE_ZONE_6 = "heart_rate_zone_6"
    DISTANCE_METER = "distance_meter"
    CALORIES = "calories"
    ELEVATION_GAIN_METER = "elevation_gain_meter"
    ELEVATION_MAXIMUM_METER = "elevation_maximum_meter"
    ELEVATION_MINIMUM_METER = "elevation_minimum_meter"
    SPEED_MEAN = "speed_mean"
    SPEED_MAXIMUM = "speed_maximum"
    POWER_SOURCE = "power_source"
    POWER_MEAN = "power_mean"
    POWER_MAXIMUM = "power_maximum"
    POWER_WEIGHTED_MEAN = "power_weighted_mean"
    STEPS = "steps"
    MAP_POLYLINE = "map_polyline"
    MAP_SUMMARY_POLYLINE = "map_summary_polyline"
    SOURCE_TYPE = "source_type"
    SOURCE_PROVIDER = "source_provider"
    SOURCE_APP_ID = "source_app_id"
    SOURCE_WORKOUT_ID = "source_workout_id"
    TIME_ZONE = "time_zone"

    def visit(
        self,
        session_start: typing.Callable[[], T_Result],
        session_end: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        sport_name: typing.Callable[[], T_Result],
        sport_slug: typing.Callable[[], T_Result],
        duration_active_second: typing.Callable[[], T_Result],
        heart_rate_mean: typing.Callable[[], T_Result],
        heart_rate_minimum: typing.Callable[[], T_Result],
        heart_rate_maximum: typing.Callable[[], T_Result],
        heart_rate_zone_1: typing.Callable[[], T_Result],
        heart_rate_zone_2: typing.Callable[[], T_Result],
        heart_rate_zone_3: typing.Callable[[], T_Result],
        heart_rate_zone_4: typing.Callable[[], T_Result],
        heart_rate_zone_5: typing.Callable[[], T_Result],
        heart_rate_zone_6: typing.Callable[[], T_Result],
        distance_meter: typing.Callable[[], T_Result],
        calories: typing.Callable[[], T_Result],
        elevation_gain_meter: typing.Callable[[], T_Result],
        elevation_maximum_meter: typing.Callable[[], T_Result],
        elevation_minimum_meter: typing.Callable[[], T_Result],
        speed_mean: typing.Callable[[], T_Result],
        speed_maximum: typing.Callable[[], T_Result],
        power_source: typing.Callable[[], T_Result],
        power_mean: typing.Callable[[], T_Result],
        power_maximum: typing.Callable[[], T_Result],
        power_weighted_mean: typing.Callable[[], T_Result],
        steps: typing.Callable[[], T_Result],
        map_polyline: typing.Callable[[], T_Result],
        map_summary_polyline: typing.Callable[[], T_Result],
        source_type: typing.Callable[[], T_Result],
        source_provider: typing.Callable[[], T_Result],
        source_app_id: typing.Callable[[], T_Result],
        source_workout_id: typing.Callable[[], T_Result],
        time_zone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkoutColumnExprWorkout.SESSION_START:
            return session_start()
        if self is WorkoutColumnExprWorkout.SESSION_END:
            return session_end()
        if self is WorkoutColumnExprWorkout.TITLE:
            return title()
        if self is WorkoutColumnExprWorkout.SPORT_NAME:
            return sport_name()
        if self is WorkoutColumnExprWorkout.SPORT_SLUG:
            return sport_slug()
        if self is WorkoutColumnExprWorkout.DURATION_ACTIVE_SECOND:
            return duration_active_second()
        if self is WorkoutColumnExprWorkout.HEART_RATE_MEAN:
            return heart_rate_mean()
        if self is WorkoutColumnExprWorkout.HEART_RATE_MINIMUM:
            return heart_rate_minimum()
        if self is WorkoutColumnExprWorkout.HEART_RATE_MAXIMUM:
            return heart_rate_maximum()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_1:
            return heart_rate_zone_1()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_2:
            return heart_rate_zone_2()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_3:
            return heart_rate_zone_3()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_4:
            return heart_rate_zone_4()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_5:
            return heart_rate_zone_5()
        if self is WorkoutColumnExprWorkout.HEART_RATE_ZONE_6:
            return heart_rate_zone_6()
        if self is WorkoutColumnExprWorkout.DISTANCE_METER:
            return distance_meter()
        if self is WorkoutColumnExprWorkout.CALORIES:
            return calories()
        if self is WorkoutColumnExprWorkout.ELEVATION_GAIN_METER:
            return elevation_gain_meter()
        if self is WorkoutColumnExprWorkout.ELEVATION_MAXIMUM_METER:
            return elevation_maximum_meter()
        if self is WorkoutColumnExprWorkout.ELEVATION_MINIMUM_METER:
            return elevation_minimum_meter()
        if self is WorkoutColumnExprWorkout.SPEED_MEAN:
            return speed_mean()
        if self is WorkoutColumnExprWorkout.SPEED_MAXIMUM:
            return speed_maximum()
        if self is WorkoutColumnExprWorkout.POWER_SOURCE:
            return power_source()
        if self is WorkoutColumnExprWorkout.POWER_MEAN:
            return power_mean()
        if self is WorkoutColumnExprWorkout.POWER_MAXIMUM:
            return power_maximum()
        if self is WorkoutColumnExprWorkout.POWER_WEIGHTED_MEAN:
            return power_weighted_mean()
        if self is WorkoutColumnExprWorkout.STEPS:
            return steps()
        if self is WorkoutColumnExprWorkout.MAP_POLYLINE:
            return map_polyline()
        if self is WorkoutColumnExprWorkout.MAP_SUMMARY_POLYLINE:
            return map_summary_polyline()
        if self is WorkoutColumnExprWorkout.SOURCE_TYPE:
            return source_type()
        if self is WorkoutColumnExprWorkout.SOURCE_PROVIDER:
            return source_provider()
        if self is WorkoutColumnExprWorkout.SOURCE_APP_ID:
            return source_app_id()
        if self is WorkoutColumnExprWorkout.SOURCE_WORKOUT_ID:
            return source_workout_id()
        if self is WorkoutColumnExprWorkout.TIME_ZONE:
            return time_zone()
