from pydantic import BaseModel # type: ignore
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ChargingProfileResponseType(str, Enum):
    ACCEPTED = "ACCEPTED"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    TOO_OFTEN = "TOO_OFTEN"
    UNKNOWN_SESSION = "UNKNOWN_SESSION"

class ChargingProfileResponse(BaseModel):
    result: ChargingProfileResponseType
    timeout: Optional[int] = None

class ChargingProfilePeriod(BaseModel):
    start_period: int 
    limit: float

class ChargingRateUnit(str, Enum):
    W = "W"
    A = "A"

class ChargingProfile(BaseModel):
    start_date_time: datetime
    duration: Optional[int] = None
    charging_rate_unit: ChargingRateUnit
    min_charging_rate: Optional[float] = None
    charging_profile_period: List[ChargingProfilePeriod]

class ActiveChargingProfile(BaseModel):
    start_date_time: datetime
    charging_profile: ChargingProfile

class ActiveChargingProfileResult(BaseModel):
    result: ChargingProfileResponseType
    profile: Optional[ActiveChargingProfile] = None

class ChargingProfileResult(BaseModel):
    result: ChargingProfileResponseType

class ClearProfileResult(BaseModel):
    result: ChargingProfileResponseType

class SetChargingProfile(BaseModel):
    response_url: str

class ChargingProfileResultType(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    UNKNOWN = "UNKNOWN"