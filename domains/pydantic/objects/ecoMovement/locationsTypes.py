from typing import List, Optional, Union
from domains.pydantic.objects.general.generalTypes import DisplayText
from domains.pydantic.objects.general.locationsRootTypes import BusinessDetails, ConnectorType, GeoLocation, Image, PowerType, ConnectorFormat
from domains.pydantic.objects.parkit.tokensRootTypes import TokenType
from pydantic import BaseModel, Field, HttpUrl # type: ignore
from datetime import datetime, time
from enum import Enum



class PublishTokenType(BaseModel):
    uid: Optional[str] = Field(None, max_length=36)
    type: Optional[TokenType]
    visual_number: Optional[str] = Field(None, max_length=64)
    issuer: Optional[str] = Field(None, max_length=64)
    group_id: Optional[str] = Field(None, max_length=36)

class AdditionalGeoLocation(BaseModel):
    latitude: str = Field(..., pattern=r'-?[0-9]{1,2}\.[0-9]{5,7}')
    longitude: str = Field(..., pattern=r'-?[0-9]{1,3}\.[0-9]{5,7}')

class Status(str, Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
    CHARGING = "CHARGING"
    INOPERATIVE = "INOPERATIVE"
    OUTOFORDER = "OUTOFORDER"
    PLANNED = "PLANNED"
    REMOVED = "REMOVED"
    RESERVED = "RESERVED"
    UNKNOWN = "UNKNOWN"

class StatusSchedule(BaseModel):
    period_begin: datetime
    period_end: Optional[datetime]
    status: Status

class Capability(str, Enum):
    CHARGING_PROFILE_CAPABLE = "CHARGING_PROFILE_CAPABLE"
    CHARGING_PREFERENCES_CAPABLE = "CHARGING_PREFERENCES_CAPABLE"
    CHIP_CARD_SUPPORT = "CHIP_CARD_SUPPORT"
    CONTACTLESS_CARD_SUPPORT = "CONTACTLESS_CARD_SUPPORT"
    CREDIT_CARD_PAYABLE = "CREDIT_CARD_PAYABLE"
    DEBIT_CARD_PAYABLE = "DEBIT_CARD_PAYABLE"
    PED_TERMINAL = "PED_TERMINAL"
    REMOTE_START_STOP_CAPABLE = "REMOTE_START_STOP_CAPABLE"
    RESERVABLE = "RESERVABLE"
    RFID_READER = "RFID_READER"
    START_SESSION_CONNECTOR_REQUIRED = "START_SESSION_CONNECTOR_REQUIRED"
    TOKEN_GROUP_CAPABLE = "TOKEN_GROUP_CAPABLE"
    UNLOCK_CAPABLE = "UNLOCK_CAPABLE"

class ParkingRestriction(str, Enum):
    EV_ONLY = "EV_ONLY"
    PLUGGED = "PLUGGED"
    DISABLED = "DISABLED"
    CUSTOMERS = "CUSTOMERS"
    MOTORCYCLES = "MOTORCYCLES"

class RegularHours(BaseModel):
    weekday: int = Field(..., ge=1, le=7)
    period_begin: time
    period_end: time

class ExceptionalPeriod(BaseModel):
    period_begin: datetime
    period_end: datetime

class Hours(BaseModel):
    twentyfourseven: bool
    regular_hours: Optional[List[RegularHours]]
    exceptional_openings: Optional[List[ExceptionalPeriod]]
    exceptional_closings: Optional[List[ExceptionalPeriod]]

class EnergySourceCategory(str, Enum):
    NUCLEAR = "NUCLEAR"
    GENERAL_FOSSIL = "GENERAL_FOSSIL"
    COAL = "COAL"
    GAS = "GAS"
    GENERAL_GREEN = "GENERAL_GREEN"
    SOLAR = "SOLAR"
    WIND = "WIND"
    WATER = "WATER"

class EnergySource(BaseModel):
    source: EnergySourceCategory
    percentage: float

class EnvironmentalImpactCategory(str, Enum):
    NUCLEAR_WASTE = "NUCLEAR_WASTE"
    CARBON_DIOXIDE = "CARBON_DIOXIDE"

class EnvironmentalImpact(BaseModel):
    category: EnvironmentalImpactCategory
    amount: float

class EnergyMix(BaseModel):
    is_green_energy: bool
    energy_sources: List[EnergySource] = Field(default_factory=list)
    environ_impact: List[EnvironmentalImpact] = Field(default_factory=list)
    supplier_name: Optional[str] = Field(None, max_length=64)
    energy_product_name: Optional[str] = Field(None, max_length=64)

class ParkingType(str, Enum):
    ALONG_MOTORWAY = "ALONG_MOTORWAY"
    PARKING_GARAGE = "PARKING_GARAGE"
    PARKING_LOT = "PARKING_LOT"
    ON_DRIVEWAY = "ON_DRIVEWAY"
    ON_STREET = "ON_STREET"
    UNDERGROUND_GARAGE = "UNDERGROUND_GARAGE"

class Facility(str, Enum):
    HOTEL = "HOTEL"
    RESTAURANT = "RESTAURANT"
    CAFE = "CAFE"
    MALL = "MALL"
    SUPERMARKET = "SUPERMARKET"
    SPORT = "SPORT"
    RECREATION_AREA = "RECREATION_AREA"
    NATURE = "NATURE"
    MUSEUM = "MUSEUM"
    BIKE_SHARING = "BIKE_SHARING"
    BUS_STOP = "BUS_STOP"
    TAXI_STAND = "TAXI_STAND"
    TRAM_STOP = "TRAM_STOP"
    METRO_STATION = "METRO_STATION"
    TRAIN_STATION = "TRAIN_STATION"
    AIRPORT = "AIRPORT"
    PARKING_LOT = "PARKING_LOT"
    CARPOOL_PARKING = "CARPOOL_PARKING"
    FUEL_STATION = "FUEL_STATION"
    WIFI = "WIFI"

""" Main ones"""
class Connector(BaseModel):
    id: str = Field(..., max_length=36)
    standard: ConnectorType
    format: ConnectorFormat
    power_type: PowerType
    max_voltage: int
    max_amperage: int
    max_electric_power: Optional[int]
    tariff_ids: List[str] = Field(default_factory=list)
    terms_and_conditions: Optional[HttpUrl]
    last_updated: datetime

class EVSE(BaseModel):
    uid: str = Field(..., max_length=36)
    evse_id: Optional[str] = Field(None, max_length=48)
    status: Status
    status_schedule: List[StatusSchedule] = Field(default_factory=list)
    capabilities: List[Capability] = Field(default_factory=list)
    connectors: List[Connector]
    floor_level: Optional[str] = Field(None, max_length=4)
    coordinates: Optional[GeoLocation]
    physical_reference: Optional[str] = Field(None, max_length=16)
    directions: List[DisplayText] = Field(default_factory=list)
    parking_restrictions: List[ParkingRestriction] = Field(default_factory=list)
    images: List[Image] = Field(default_factory=list)
    last_updated: datetime


class Location(BaseModel):
    country_code: str = Field(..., max_length=3)
    party_id: str = Field(..., max_length=3)
    id: str = Field(..., max_length=36)
    publish: bool
    publish_allowed_to: List[PublishTokenType] = Field(default_factory=list)
    name: Optional[str] = Field(None, max_length=255)
    address: str = Field(..., max_length=45)
    city: str = Field(..., max_length=45)
    postal_code: Optional[str] = Field(None, max_length=10)
    state: Optional[str] = Field(None, max_length=20)
    country: str = Field(..., max_length=3)
    coordinates: GeoLocation
    related_locations: List[AdditionalGeoLocation] = Field(default_factory=list)
    parking_type: Optional[ParkingType]
    evses: List[EVSE] = Field(default_factory=list)
    directions: List[DisplayText] = Field(default_factory=list)
    operator: Optional[BusinessDetails]
    suboperator: Optional[BusinessDetails]
    owner: Optional[BusinessDetails]
    facilities: List[Facility] = Field(default_factory=list)
    time_zone: str = Field(..., max_length=255)
    opening_times: Optional[Hours]
    charging_when_closed: Optional[bool]
    images: List[Image] = Field(default_factory=list)
    energy_mix: Optional[EnergyMix]
    last_updated: datetime