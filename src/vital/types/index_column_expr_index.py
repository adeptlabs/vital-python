# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IndexColumnExprIndex(str, enum.Enum):
    SLEEP = "sleep"
    ACTIVITY = "activity"
    WORKOUT = "workout"
    BODY = "body"

    def visit(
        self,
        sleep: typing.Callable[[], T_Result],
        activity: typing.Callable[[], T_Result],
        workout: typing.Callable[[], T_Result],
        body: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IndexColumnExprIndex.SLEEP:
            return sleep()
        if self is IndexColumnExprIndex.ACTIVITY:
            return activity()
        if self is IndexColumnExprIndex.WORKOUT:
            return workout()
        if self is IndexColumnExprIndex.BODY:
            return body()
