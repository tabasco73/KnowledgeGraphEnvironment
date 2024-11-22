from domains.pydantic.objects.parkit.tariffsRootTypes import ReservationRestrictionType
from domains.pydantic.objects.general.generalTypes import DisplayText, Price
from pydantic import BaseModel, Field # type: ignore
from typing import Optional, List
from datetime import datetime
from enum import Enum

class DayOfWeek(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

class TariffRestrictions(BaseModel):
    start_time: Optional[str] = Field(None, max_length=5)  # Time in HH:MM format
    end_time: Optional[str] = Field(None, max_length=5)  # Time in HH:MM format
    start_date: Optional[str] = Field(None, max_length=10)  # Date in YYYY-MM-DD format
    end_date: Optional[str] = Field(None, max_length=10)  # Date in YYYY-MM-DD format
    min_kwh: Optional[float] = None
    max_kwh: Optional[float] = None
    min_current: Optional[float] = None  # Assuming current is measured in A (Amperes)
    max_current: Optional[float] = None
    min_power: Optional[float] = None  # Assuming power is measured in kW (Kilowatts)
    max_power: Optional[float] = None
    min_duration: Optional[int] = None  # Duration in seconds
    max_duration: Optional[int] = None  # Duration in seconds
    day_of_week: Optional[List[DayOfWeek]] = None  # Assuming DayOfWeek is an enum defined earlier
    reservation: Optional[ReservationRestrictionType] = None