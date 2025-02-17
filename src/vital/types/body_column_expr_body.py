# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BodyColumnExprBody(str, enum.Enum):
    MEASURED_AT = "measured_at"
    WEIGHT_KILOGRAM = "weight_kilogram"
    FAT_MASS_PERCENTAGE = "fat_mass_percentage"
    WATER_PERCENTAGE = "water_percentage"
    MUSCLE_MASS_PERCENTAGE = "muscle_mass_percentage"
    VISCERAL_FAT_INDEX = "visceral_fat_index"
    BONE_MASS_PERCENTAGE = "bone_mass_percentage"
    SOURCE_TYPE = "source_type"
    SOURCE_PROVIDER = "source_provider"
    SOURCE_APP_ID = "source_app_id"
    TIME_ZONE = "time_zone"

    def visit(
        self,
        measured_at: typing.Callable[[], T_Result],
        weight_kilogram: typing.Callable[[], T_Result],
        fat_mass_percentage: typing.Callable[[], T_Result],
        water_percentage: typing.Callable[[], T_Result],
        muscle_mass_percentage: typing.Callable[[], T_Result],
        visceral_fat_index: typing.Callable[[], T_Result],
        bone_mass_percentage: typing.Callable[[], T_Result],
        source_type: typing.Callable[[], T_Result],
        source_provider: typing.Callable[[], T_Result],
        source_app_id: typing.Callable[[], T_Result],
        time_zone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BodyColumnExprBody.MEASURED_AT:
            return measured_at()
        if self is BodyColumnExprBody.WEIGHT_KILOGRAM:
            return weight_kilogram()
        if self is BodyColumnExprBody.FAT_MASS_PERCENTAGE:
            return fat_mass_percentage()
        if self is BodyColumnExprBody.WATER_PERCENTAGE:
            return water_percentage()
        if self is BodyColumnExprBody.MUSCLE_MASS_PERCENTAGE:
            return muscle_mass_percentage()
        if self is BodyColumnExprBody.VISCERAL_FAT_INDEX:
            return visceral_fat_index()
        if self is BodyColumnExprBody.BONE_MASS_PERCENTAGE:
            return bone_mass_percentage()
        if self is BodyColumnExprBody.SOURCE_TYPE:
            return source_type()
        if self is BodyColumnExprBody.SOURCE_PROVIDER:
            return source_provider()
        if self is BodyColumnExprBody.SOURCE_APP_ID:
            return source_app_id()
        if self is BodyColumnExprBody.TIME_ZONE:
            return time_zone()
