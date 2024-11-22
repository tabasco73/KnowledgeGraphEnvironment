from typing import List, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field # type: ignore

from domains.pydantic.objects.parkit.tokensRootTypes import TokenType

class CdrDimensionType(str, Enum):
    CURRENT = "CURRENT"
    ENERGY = "ENERGY"
    ENERGY_EXPORT = "ENERGY_EXPORT"
    ENERGY_IMPORT = "ENERGY_IMPORT"
    MAX_CURRENT = "MAX_CURRENT"
    MIN_CURRENT = "MIN_CURRENT"
    MAX_POWER = "MAX_POWER"
    MIN_POWER = "MIN_POWER"
    PARKING_TIME = "PARKING_TIME"
    POWER = "POWER"
    RESERVATION_TIME = "RESERVATION_TIME"
    STATE_OF_CHARGE = "STATE_OF_CHARGE"
    TIME = "TIME"

class CdrDimension(BaseModel):
    type: CdrDimensionType
    volume: float

class ChargingPeriod(BaseModel):
    start_date_time: datetime
    dimensions: List[CdrDimension] 
    tariff_id: Optional[str] = Field(None, max_length=36)

class AuthMethod(str, Enum):
    AUTH_REQUEST = "AUTH_REQUEST"
    COMMAND = "COMMAND"
    WHITELIST = "WHITELIST"

class CdrToken(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    uid: str = Field(..., max_length=36)
    type: TokenType
    contract_id: Optional[str] = Field(None, max_length=36)