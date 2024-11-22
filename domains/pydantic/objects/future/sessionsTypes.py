
from enum import Enum
from typing import List, Optional
from domains.pydantic.objects.general.generalTypes import Price
from domains.pydantic.objects.parkit.cDRsRootTypes import AuthMethod, CdrToken, ChargingPeriod
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime

from domains.pydantic.objects.parkit.sessionsTypes import ChargingPreferencesResponse, ProfileType, Session

class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    INVALID = "INVALID"
    PENDING = "PENDING"
    RESERVATION = "RESERVATION"

class Session(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    id: str = Field(..., max_length=36)
    start_date_time: datetime
    end_date_time: Optional[datetime] = None
    kwh: float
    cdr_token: CdrToken
    auth_method: Optional[AuthMethod] = None  # This should be an Enum if defined
    authorization_reference: Optional[str] = Field(None, max_length=36)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)
    meter_id: Optional[str] = Field(None, max_length=255)
    currency: str = Field(..., max_length=3)
    charging_periods: Optional[List[ChargingPeriod]] = Field(default_factory=list)
    total_cost: Optional[Price] = None
    status: Optional[SessionStatus] = None
    last_updated: datetime

class ChargingPreferences(BaseModel):
    profile_type: ProfileType  # This should be an Enum, assumed to be 'ProfileType'
    departure_time: Optional[datetime] = None
    energy_need: Optional[float] = None
    discharge_allowed: Optional[bool] = None

class ChargingPreferencesResponse(str, Enum):
    ACCEPTED = "ACCEPTED"
    DEPARTURE_REQUIRED = "DEPARTURE_REQUIRED"
    ENERGY_NEED_REQUIRED = "ENERGY_NEED_REQUIRED"
    NOT_POSSIBLE = "NOT_POSSIBLE"
    PROFILE_TYPE_NOT_SUPPORTED = "PROFILE_TYPE_NOT_SUPPORTED"

""" Sender Interface - CPO Implements """
# PUT

class PutSessionsSenderRequestParams(BaseModel):
    session_id: str = Field(..., max_length=36)

class PutSessionsSenderRequestBody(BaseModel):
    ChargingPreferences: ChargingPreferences  # Assuming ChargingPreferences is a custom class

class PutSessionsSenderResponse(BaseModel):
    response: ChargingPreferencesResponse  # Assuming ChargingPreferencesResponse is a custom class or enum
