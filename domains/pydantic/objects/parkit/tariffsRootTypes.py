from pydantic import BaseModel, Field # type: ignore
from typing import Optional, List
from datetime import datetime
from enum import Enum

from domains.pydantic.objects.general.generalTypes import DisplayText, Price

class ReservationRestrictionType(str, Enum):
    RESERVATION = "RESERVATION"
    RESERVATION_EXPIRES = "RESERVATION_EXPIRES"

class TariffDimensionType(str, Enum):
    ENERGY = "ENERGY"
    FLAT = "FLAT"
    PARKING_TIME = "PARKING_TIME"
    TIME = "TIME"

class PriceComponent(BaseModel):
    type: TariffDimensionType
    price: float
    vat: Optional[float] = None
    step_size: int

class TariffType(str, Enum):
    AD_HOC_PAYMENT = "AD_HOC_PAYMENT"
    PROFILE_CHEAP = "PROFILE_CHEAP"
    PROFILE_FAST = "PROFILE_FAST"
    PROFILE_GREEN = "PROFILE_GREEN"
    REGULAR = "REGULAR"

class TariffElement(BaseModel):
    price_components: List[PriceComponent]
    restrictions: Optional[ReservationRestrictionType] = None

class Tariff(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    id: str = Field(..., max_length=36)
    currency: str = Field(..., max_length=3)
    type: Optional[TariffType] = None
    tariff_alt_text: Optional[List[DisplayText]] = Field(default_factory=list)
    tariff_alt_url: Optional[str] = None
    min_price: Optional[Price] = None
    max_price: Optional[Price] = None
    elements: List[TariffElement] = Field(default_factory=list)
    start_date_time: Optional[datetime] = None
    end_date_time: Optional[datetime] = None
    energy_mix: Optional[str] = None
    last_updated: datetime