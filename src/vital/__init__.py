# This file was auto-generated by Fern from our API Definition.

from .types import (
    ActivitySelector,
    ActivitySelectorActivity,
    ActivityV2InDb,
    Address,
    AllowedRadius,
    Answer,
    AoE,
    AoEAnswer,
    AppointmentAvailabilitySlots,
    AppointmentEventStatus,
    AppointmentProvider,
    AppointmentServiceType,
    AppointmentStatus,
    AppointmentType,
    AreaInfo,
    AttemptStatus,
    AuthType,
    Availability,
    BasalBodyTemperatureEntry,
    Billing,
    BiomarkerResult,
    BodyV2InDb,
    CervicalMucusEntry,
    CervicalMucusEntryQuality,
    ClientActivityResponse,
    ClientBodyResponse,
    ClientFacingActivity,
    ClientFacingApiKey,
    ClientFacingAppointment,
    ClientFacingAppointmentCancellationReason,
    ClientFacingAppointmentEvent,
    ClientFacingAtHomePhlebotomyOrder,
    ClientFacingAtHomePhlebotomyOrderDetails,
    ClientFacingBloodOxygenTimeseries,
    ClientFacingBloodPressureTimeseries,
    ClientFacingBody,
    ClientFacingBodyFatTimeseries,
    ClientFacingBodyTemperatureDeltaSample,
    ClientFacingBodyTemperatureDeltaSampleSensorLocation,
    ClientFacingBodyTemperatureSample,
    ClientFacingBodyTemperatureSampleSensorLocation,
    ClientFacingBodyWeightTimeseries,
    ClientFacingCaffeineTimeseries,
    ClientFacingCaloriesActiveTimeseries,
    ClientFacingCaloriesBasalTimeseries,
    ClientFacingCarbohydratesSample,
    ClientFacingCholesterolTimeseries,
    ClientFacingDiagnosisInformation,
    ClientFacingDistanceTimeseries,
    ClientFacingElectrocardiogramVoltageTimeseries,
    ClientFacingFloorsClimbedTimeseries,
    ClientFacingFood,
    ClientFacingGlucoseTimeseries,
    ClientFacingGroupedTimeseriesResponseClientFacingBodyTemperatureDeltaSample,
    ClientFacingGroupedTimeseriesResponseClientFacingBodyTemperatureSample,
    ClientFacingGroupedTimeseriesResponseClientFacingCarbohydratesSample,
    ClientFacingGroupedTimeseriesResponseClientFacingInsulinInjectionSample,
    ClientFacingGroupedTimeseriesResponseClientFacingNoteSample,
    ClientFacingGroupedTimeseriesResponseClientFacingWorkoutDurationSample,
    ClientFacingHeartRate,
    ClientFacingHeartRateTimeseries,
    ClientFacingHrvTimeseries,
    ClientFacingHypnogramTimeseries,
    ClientFacingIgeTimeseries,
    ClientFacingIggTimeseries,
    ClientFacingInsulinInjectionSample,
    ClientFacingInsulinInjectionSampleType,
    ClientFacingInsurance,
    ClientFacingLab,
    ClientFacingLabLocation,
    ClientFacingLabTest,
    ClientFacingLabs,
    ClientFacingLoinc,
    ClientFacingMarker,
    ClientFacingMarkerComplete,
    ClientFacingMealResponse,
    ClientFacingMindfulnessMinutesTimeseries,
    ClientFacingNoteSample,
    ClientFacingNoteSampleTagsItem,
    ClientFacingOrder,
    ClientFacingOrderDetails,
    ClientFacingOrderDetails_AtHomePhlebotomy,
    ClientFacingOrderDetails_Testkit,
    ClientFacingOrderDetails_WalkInTest,
    ClientFacingOrderEvent,
    ClientFacingPatientDetailsCompatible,
    ClientFacingPayorSearchResponse,
    ClientFacingPhysician,
    ClientFacingProfile,
    ClientFacingProvider,
    ClientFacingProviderDetailed,
    ClientFacingProviderWithStatus,
    ClientFacingResource,
    ClientFacingRespiratoryRateTimeseries,
    ClientFacingResult,
    ClientFacingSampleGroupingKeys,
    ClientFacingShipment,
    ClientFacingSleep,
    ClientFacingSleepStream,
    ClientFacingSource,
    ClientFacingSport,
    ClientFacingStepsTimeseries,
    ClientFacingStream,
    ClientFacingStreamAltitude,
    ClientFacingStreamCadence,
    ClientFacingStreamDistance,
    ClientFacingStreamHeartrate,
    ClientFacingStreamLat,
    ClientFacingStreamLng,
    ClientFacingStreamPower,
    ClientFacingStreamResistance,
    ClientFacingStreamTemperature,
    ClientFacingStreamVelocitySmooth,
    ClientFacingStressLevelTimeseries,
    ClientFacingTeam,
    ClientFacingTestKitOrderDetails,
    ClientFacingTestkitOrder,
    ClientFacingTimeseriesGroupClientFacingBodyTemperatureDeltaSample,
    ClientFacingTimeseriesGroupClientFacingBodyTemperatureSample,
    ClientFacingTimeseriesGroupClientFacingCarbohydratesSample,
    ClientFacingTimeseriesGroupClientFacingInsulinInjectionSample,
    ClientFacingTimeseriesGroupClientFacingNoteSample,
    ClientFacingTimeseriesGroupClientFacingWorkoutDurationSample,
    ClientFacingUser,
    ClientFacingUserKey,
    ClientFacingVo2MaxTimeseries,
    ClientFacingWalkInOrderDetails,
    ClientFacingWalkInTestOrder,
    ClientFacingWaterTimeseries,
    ClientFacingWorkout,
    ClientFacingWorkoutDurationSample,
    ClientFacingWorkoutDurationSampleIntensity,
    ClientSleepResponse,
    ClientUserIdConflict,
    ClientWorkoutResponse,
    CompanyDetails,
    ConnectedSourceClientFacing,
    ConnectionStatus,
    ConnectionStatusState,
    Consent,
    ConsentType,
    ContraceptiveEntry,
    ContraceptiveEntryType,
    DateTimeUnit,
    DaySlots,
    DelegatedFlowType,
    DemoConnectionStatus,
    DemoProviders,
    DetectedDeviationEntry,
    DetectedDeviationEntryDeviation,
    DeviceV2InDb,
    EmailProviders,
    Energy,
    EventDestinationPreferences,
    EventDestinationPreferencesEnabledItem,
    EventDestinationPreferencesPreferred,
    FallbackBirthDate,
    FallbackTimeZone,
    Fats,
    Gender,
    GetMarkersResponse,
    GetOrdersResponse,
    GroupedBloodOxygen,
    GroupedBloodOxygenResponse,
    GroupedBloodPressure,
    GroupedBloodPressureResponse,
    GroupedBodyFat,
    GroupedBodyFatResponse,
    GroupedBodyWeight,
    GroupedBodyWeightResponse,
    GroupedCaffeine,
    GroupedCaffeineResponse,
    GroupedCaloriesActive,
    GroupedCaloriesActiveResponse,
    GroupedCaloriesBasal,
    GroupedCaloriesBasalResponse,
    GroupedCholesterol,
    GroupedCholesterolResponse,
    GroupedDistance,
    GroupedDistanceResponse,
    GroupedElectrocardiogramVoltage,
    GroupedElectrocardiogramVoltageResponse,
    GroupedFloorsClimbed,
    GroupedFloorsClimbedResponse,
    GroupedGlucose,
    GroupedGlucoseResponse,
    GroupedHeartRate,
    GroupedHeartRateResponse,
    GroupedHrv,
    GroupedHrvResponse,
    GroupedHypnogram,
    GroupedHypnogramResponse,
    GroupedIge,
    GroupedIgeResponse,
    GroupedIgg,
    GroupedIggResponse,
    GroupedMindfulnessMinutes,
    GroupedMindfulnessMinutesResponse,
    GroupedRespiratoryRate,
    GroupedRespiratoryRateResponse,
    GroupedSteps,
    GroupedStepsResponse,
    GroupedStressLevel,
    GroupedStressLevelResponse,
    GroupedVo2Max,
    GroupedVo2MaxResponse,
    GroupedWater,
    GroupedWaterResponse,
    HealthInsuranceCreateRequest,
    HealthInsuranceCreateRequestBackImage,
    HealthInsuranceCreateRequestFrontImage,
    HealthInsuranceCreateRequestPatientSignatureImage,
    HistoricalPullStatus,
    HistoricalPullTimeline,
    HomePregnancyTestEntry,
    HomePregnancyTestEntryTestResult,
    HomeProgesteroneTestEntry,
    HomeProgesteroneTestEntryTestResult,
    HttpValidationError,
    IntermenstrualBleedingEntry,
    Jpeg,
    LabLocationMetadata,
    LabResultsMetadata,
    LabResultsRaw,
    LabResultsRawResults,
    LabTestCollectionMethod,
    LabTestSampleType,
    LabTestStatus,
    Labs,
    LastAttempt,
    LibreConfig,
    LinkTokenExchangeResponse,
    LngLat,
    Macros,
    ManualProviders,
    MarkerType,
    MealInDbBaseClientFacingSource,
    MenstrualCycle,
    MenstrualCycleResponse,
    MenstrualFlowEntry,
    MenstrualFlowEntryFlow,
    MetricsResult,
    Micros,
    OAuthProviders,
    OrderStatus,
    OrderTopLevelStatus,
    OvulationTestEntry,
    OvulationTestEntryTestResult,
    PaginatedUsersResponse,
    PasswordProviders,
    PatientAddressCompatible,
    PatientDetails,
    Period,
    PersonDetailsOutput,
    PhlebotomyAreaInfo,
    PhlebotomyProviderInfo,
    PhysicianCreateRequest,
    PhysicianCreateRequestBase,
    PhysicianCreateRequestSignatureImage,
    Png,
    PostOrderResponse,
    ProfileInDb,
    ProviderLinkResponse,
    ProviderLinkResponseState,
    ProviderMfaRequest,
    ProviderMfaRequestMethod,
    Providers,
    PscAreaInfo,
    PscAreaInfoDetails,
    PscInfo,
    QueryConfig,
    QueryConfigProviderPriorityOverridesItem,
    QueryConfigWeekStartsOn,
    QueryInstruction,
    QueryInstructionPartitionBy,
    QueryInstructionSelect,
    QueryInstructionSwizzleBy,
    Question,
    QuestionType,
    RawActivity,
    RawBody,
    RawDevices,
    RawProfile,
    RawSleep,
    RawWorkout,
    Reducer,
    ReducerFunction,
    Region,
    RelativeTimeframe,
    ResourceAvailability,
    ResponsibleRelationship,
    ResultType,
    ScopeRequirementsGrants,
    ScopeRequirementsStr,
    SessionPartitioning,
    SessionPartitioningSession,
    SexualActivityEntry,
    ShippingAddress,
    SingleHistoricalPullStatistics,
    SingleProviderHistoricalPullResponse,
    SingleResourceStatistics,
    SingleUserHistoricalPullResponse,
    SingleUserResourceResponse,
    SleepSelector,
    SleepSelectorSleep,
    SleepSummaryState,
    SleepV2InDb,
    Source,
    SourceAuthType,
    SourceLink,
    SourceType,
    Swizzling,
    SwizzlingBinGranularity,
    TeamConfig,
    TimeSlot,
    TimeseriesMetricPoint,
    TimeseriesResource,
    UsAddress,
    UserHistoricalPullsResponse,
    UserInfo,
    UserRefreshErrorResponse,
    UserRefreshSuccessResponse,
    UserResourcesResponse,
    UserSignInTokenResponse,
    UserSuccessResponse,
    ValidationError,
    ValidationErrorLocItem,
    VitalCoreSchemasDbSchemasLabTestHealthInsurancePersonDetails,
    VitalCoreSchemasDbSchemasLabTestInsurancePersonDetails,
    VitalTokenCreatedResponse,
    WorkoutV2InDb,
)
from .errors import BadRequestError, UnprocessableEntityError
from .resources import (
    LabTestsGetOrdersRequestOrderDirection,
    LabTestsGetOrdersRequestOrderKey,
    activity,
    aggregate,
    body,
    devices,
    insurance,
    introspect,
    lab_tests,
    link,
    meal,
    menstrual_cycle,
    profile,
    providers,
    sleep,
    team,
    testkit,
    user,
    vitals,
    workouts,
)
from .environment import VitalEnvironment

__all__ = [
    "ActivitySelector",
    "ActivitySelectorActivity",
    "ActivityV2InDb",
    "Address",
    "AllowedRadius",
    "Answer",
    "AoE",
    "AoEAnswer",
    "AppointmentAvailabilitySlots",
    "AppointmentEventStatus",
    "AppointmentProvider",
    "AppointmentServiceType",
    "AppointmentStatus",
    "AppointmentType",
    "AreaInfo",
    "AttemptStatus",
    "AuthType",
    "Availability",
    "BadRequestError",
    "BasalBodyTemperatureEntry",
    "Billing",
    "BiomarkerResult",
    "BodyV2InDb",
    "CervicalMucusEntry",
    "CervicalMucusEntryQuality",
    "ClientActivityResponse",
    "ClientBodyResponse",
    "ClientFacingActivity",
    "ClientFacingApiKey",
    "ClientFacingAppointment",
    "ClientFacingAppointmentCancellationReason",
    "ClientFacingAppointmentEvent",
    "ClientFacingAtHomePhlebotomyOrder",
    "ClientFacingAtHomePhlebotomyOrderDetails",
    "ClientFacingBloodOxygenTimeseries",
    "ClientFacingBloodPressureTimeseries",
    "ClientFacingBody",
    "ClientFacingBodyFatTimeseries",
    "ClientFacingBodyTemperatureDeltaSample",
    "ClientFacingBodyTemperatureDeltaSampleSensorLocation",
    "ClientFacingBodyTemperatureSample",
    "ClientFacingBodyTemperatureSampleSensorLocation",
    "ClientFacingBodyWeightTimeseries",
    "ClientFacingCaffeineTimeseries",
    "ClientFacingCaloriesActiveTimeseries",
    "ClientFacingCaloriesBasalTimeseries",
    "ClientFacingCarbohydratesSample",
    "ClientFacingCholesterolTimeseries",
    "ClientFacingDiagnosisInformation",
    "ClientFacingDistanceTimeseries",
    "ClientFacingElectrocardiogramVoltageTimeseries",
    "ClientFacingFloorsClimbedTimeseries",
    "ClientFacingFood",
    "ClientFacingGlucoseTimeseries",
    "ClientFacingGroupedTimeseriesResponseClientFacingBodyTemperatureDeltaSample",
    "ClientFacingGroupedTimeseriesResponseClientFacingBodyTemperatureSample",
    "ClientFacingGroupedTimeseriesResponseClientFacingCarbohydratesSample",
    "ClientFacingGroupedTimeseriesResponseClientFacingInsulinInjectionSample",
    "ClientFacingGroupedTimeseriesResponseClientFacingNoteSample",
    "ClientFacingGroupedTimeseriesResponseClientFacingWorkoutDurationSample",
    "ClientFacingHeartRate",
    "ClientFacingHeartRateTimeseries",
    "ClientFacingHrvTimeseries",
    "ClientFacingHypnogramTimeseries",
    "ClientFacingIgeTimeseries",
    "ClientFacingIggTimeseries",
    "ClientFacingInsulinInjectionSample",
    "ClientFacingInsulinInjectionSampleType",
    "ClientFacingInsurance",
    "ClientFacingLab",
    "ClientFacingLabLocation",
    "ClientFacingLabTest",
    "ClientFacingLabs",
    "ClientFacingLoinc",
    "ClientFacingMarker",
    "ClientFacingMarkerComplete",
    "ClientFacingMealResponse",
    "ClientFacingMindfulnessMinutesTimeseries",
    "ClientFacingNoteSample",
    "ClientFacingNoteSampleTagsItem",
    "ClientFacingOrder",
    "ClientFacingOrderDetails",
    "ClientFacingOrderDetails_AtHomePhlebotomy",
    "ClientFacingOrderDetails_Testkit",
    "ClientFacingOrderDetails_WalkInTest",
    "ClientFacingOrderEvent",
    "ClientFacingPatientDetailsCompatible",
    "ClientFacingPayorSearchResponse",
    "ClientFacingPhysician",
    "ClientFacingProfile",
    "ClientFacingProvider",
    "ClientFacingProviderDetailed",
    "ClientFacingProviderWithStatus",
    "ClientFacingResource",
    "ClientFacingRespiratoryRateTimeseries",
    "ClientFacingResult",
    "ClientFacingSampleGroupingKeys",
    "ClientFacingShipment",
    "ClientFacingSleep",
    "ClientFacingSleepStream",
    "ClientFacingSource",
    "ClientFacingSport",
    "ClientFacingStepsTimeseries",
    "ClientFacingStream",
    "ClientFacingStreamAltitude",
    "ClientFacingStreamCadence",
    "ClientFacingStreamDistance",
    "ClientFacingStreamHeartrate",
    "ClientFacingStreamLat",
    "ClientFacingStreamLng",
    "ClientFacingStreamPower",
    "ClientFacingStreamResistance",
    "ClientFacingStreamTemperature",
    "ClientFacingStreamVelocitySmooth",
    "ClientFacingStressLevelTimeseries",
    "ClientFacingTeam",
    "ClientFacingTestKitOrderDetails",
    "ClientFacingTestkitOrder",
    "ClientFacingTimeseriesGroupClientFacingBodyTemperatureDeltaSample",
    "ClientFacingTimeseriesGroupClientFacingBodyTemperatureSample",
    "ClientFacingTimeseriesGroupClientFacingCarbohydratesSample",
    "ClientFacingTimeseriesGroupClientFacingInsulinInjectionSample",
    "ClientFacingTimeseriesGroupClientFacingNoteSample",
    "ClientFacingTimeseriesGroupClientFacingWorkoutDurationSample",
    "ClientFacingUser",
    "ClientFacingUserKey",
    "ClientFacingVo2MaxTimeseries",
    "ClientFacingWalkInOrderDetails",
    "ClientFacingWalkInTestOrder",
    "ClientFacingWaterTimeseries",
    "ClientFacingWorkout",
    "ClientFacingWorkoutDurationSample",
    "ClientFacingWorkoutDurationSampleIntensity",
    "ClientSleepResponse",
    "ClientUserIdConflict",
    "ClientWorkoutResponse",
    "CompanyDetails",
    "ConnectedSourceClientFacing",
    "ConnectionStatus",
    "ConnectionStatusState",
    "Consent",
    "ConsentType",
    "ContraceptiveEntry",
    "ContraceptiveEntryType",
    "DateTimeUnit",
    "DaySlots",
    "DelegatedFlowType",
    "DemoConnectionStatus",
    "DemoProviders",
    "DetectedDeviationEntry",
    "DetectedDeviationEntryDeviation",
    "DeviceV2InDb",
    "EmailProviders",
    "Energy",
    "EventDestinationPreferences",
    "EventDestinationPreferencesEnabledItem",
    "EventDestinationPreferencesPreferred",
    "FallbackBirthDate",
    "FallbackTimeZone",
    "Fats",
    "Gender",
    "GetMarkersResponse",
    "GetOrdersResponse",
    "GroupedBloodOxygen",
    "GroupedBloodOxygenResponse",
    "GroupedBloodPressure",
    "GroupedBloodPressureResponse",
    "GroupedBodyFat",
    "GroupedBodyFatResponse",
    "GroupedBodyWeight",
    "GroupedBodyWeightResponse",
    "GroupedCaffeine",
    "GroupedCaffeineResponse",
    "GroupedCaloriesActive",
    "GroupedCaloriesActiveResponse",
    "GroupedCaloriesBasal",
    "GroupedCaloriesBasalResponse",
    "GroupedCholesterol",
    "GroupedCholesterolResponse",
    "GroupedDistance",
    "GroupedDistanceResponse",
    "GroupedElectrocardiogramVoltage",
    "GroupedElectrocardiogramVoltageResponse",
    "GroupedFloorsClimbed",
    "GroupedFloorsClimbedResponse",
    "GroupedGlucose",
    "GroupedGlucoseResponse",
    "GroupedHeartRate",
    "GroupedHeartRateResponse",
    "GroupedHrv",
    "GroupedHrvResponse",
    "GroupedHypnogram",
    "GroupedHypnogramResponse",
    "GroupedIge",
    "GroupedIgeResponse",
    "GroupedIgg",
    "GroupedIggResponse",
    "GroupedMindfulnessMinutes",
    "GroupedMindfulnessMinutesResponse",
    "GroupedRespiratoryRate",
    "GroupedRespiratoryRateResponse",
    "GroupedSteps",
    "GroupedStepsResponse",
    "GroupedStressLevel",
    "GroupedStressLevelResponse",
    "GroupedVo2Max",
    "GroupedVo2MaxResponse",
    "GroupedWater",
    "GroupedWaterResponse",
    "HealthInsuranceCreateRequest",
    "HealthInsuranceCreateRequestBackImage",
    "HealthInsuranceCreateRequestFrontImage",
    "HealthInsuranceCreateRequestPatientSignatureImage",
    "HistoricalPullStatus",
    "HistoricalPullTimeline",
    "HomePregnancyTestEntry",
    "HomePregnancyTestEntryTestResult",
    "HomeProgesteroneTestEntry",
    "HomeProgesteroneTestEntryTestResult",
    "HttpValidationError",
    "IntermenstrualBleedingEntry",
    "Jpeg",
    "LabLocationMetadata",
    "LabResultsMetadata",
    "LabResultsRaw",
    "LabResultsRawResults",
    "LabTestCollectionMethod",
    "LabTestSampleType",
    "LabTestStatus",
    "LabTestsGetOrdersRequestOrderDirection",
    "LabTestsGetOrdersRequestOrderKey",
    "Labs",
    "LastAttempt",
    "LibreConfig",
    "LinkTokenExchangeResponse",
    "LngLat",
    "Macros",
    "ManualProviders",
    "MarkerType",
    "MealInDbBaseClientFacingSource",
    "MenstrualCycle",
    "MenstrualCycleResponse",
    "MenstrualFlowEntry",
    "MenstrualFlowEntryFlow",
    "MetricsResult",
    "Micros",
    "OAuthProviders",
    "OrderStatus",
    "OrderTopLevelStatus",
    "OvulationTestEntry",
    "OvulationTestEntryTestResult",
    "PaginatedUsersResponse",
    "PasswordProviders",
    "PatientAddressCompatible",
    "PatientDetails",
    "Period",
    "PersonDetailsOutput",
    "PhlebotomyAreaInfo",
    "PhlebotomyProviderInfo",
    "PhysicianCreateRequest",
    "PhysicianCreateRequestBase",
    "PhysicianCreateRequestSignatureImage",
    "Png",
    "PostOrderResponse",
    "ProfileInDb",
    "ProviderLinkResponse",
    "ProviderLinkResponseState",
    "ProviderMfaRequest",
    "ProviderMfaRequestMethod",
    "Providers",
    "PscAreaInfo",
    "PscAreaInfoDetails",
    "PscInfo",
    "QueryConfig",
    "QueryConfigProviderPriorityOverridesItem",
    "QueryConfigWeekStartsOn",
    "QueryInstruction",
    "QueryInstructionPartitionBy",
    "QueryInstructionSelect",
    "QueryInstructionSwizzleBy",
    "Question",
    "QuestionType",
    "RawActivity",
    "RawBody",
    "RawDevices",
    "RawProfile",
    "RawSleep",
    "RawWorkout",
    "Reducer",
    "ReducerFunction",
    "Region",
    "RelativeTimeframe",
    "ResourceAvailability",
    "ResponsibleRelationship",
    "ResultType",
    "ScopeRequirementsGrants",
    "ScopeRequirementsStr",
    "SessionPartitioning",
    "SessionPartitioningSession",
    "SexualActivityEntry",
    "ShippingAddress",
    "SingleHistoricalPullStatistics",
    "SingleProviderHistoricalPullResponse",
    "SingleResourceStatistics",
    "SingleUserHistoricalPullResponse",
    "SingleUserResourceResponse",
    "SleepSelector",
    "SleepSelectorSleep",
    "SleepSummaryState",
    "SleepV2InDb",
    "Source",
    "SourceAuthType",
    "SourceLink",
    "SourceType",
    "Swizzling",
    "SwizzlingBinGranularity",
    "TeamConfig",
    "TimeSlot",
    "TimeseriesMetricPoint",
    "TimeseriesResource",
    "UnprocessableEntityError",
    "UsAddress",
    "UserHistoricalPullsResponse",
    "UserInfo",
    "UserRefreshErrorResponse",
    "UserRefreshSuccessResponse",
    "UserResourcesResponse",
    "UserSignInTokenResponse",
    "UserSuccessResponse",
    "ValidationError",
    "ValidationErrorLocItem",
    "VitalCoreSchemasDbSchemasLabTestHealthInsurancePersonDetails",
    "VitalCoreSchemasDbSchemasLabTestInsurancePersonDetails",
    "VitalEnvironment",
    "VitalTokenCreatedResponse",
    "WorkoutV2InDb",
    "activity",
    "aggregate",
    "body",
    "devices",
    "insurance",
    "introspect",
    "lab_tests",
    "link",
    "meal",
    "menstrual_cycle",
    "profile",
    "providers",
    "sleep",
    "team",
    "testkit",
    "user",
    "vitals",
    "workouts",
]
