from typing import List, Optional, Union
from domains.pydantic.objects.general.generalTypes import Price 
from domains.pydantic.objects.general.locationsRootTypes import ConnectorFormat, ConnectorType, GeoLocation, PowerType
from domains.pydantic.objects.parkit.cDRsRootTypes import AuthMethod, CdrToken, ChargingPeriod
from domains.pydantic.objects.parkit.tariffsRootTypes import Tariff
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime

class SignedValue(BaseModel):
    nature: str = Field(..., max_length=32)
    plain_data: str = Field(..., max_length=512)
    signed_data: str = Field(..., max_length=5000)
    
class SignedData(BaseModel):
    encoding_method: str = Field(..., max_length=36)
    encoding_method_version: Optional[int] = None
    public_key: Optional[str] = Field(None, max_length=512)
    signed_values: List[SignedValue]  # Assuming SignedValue is another class
    url: Optional[str] = Field(None, max_length=512)

class CdrLocation(BaseModel):
    id: str = Field(..., max_length=36)
    name: Optional[str] = Field(None, max_length=255)
    address: str = Field(..., max_length=45)
    city: str = Field(..., max_length=45)
    postal_code: Optional[str] = Field(None, max_length=10)
    state: Optional[str] = Field(None, max_length=20)
    country: str = Field(..., max_length=3)
    coordinates: GeoLocation
    evse_uid: str = Field(..., max_length=48)
    evse_id: str = Field(..., max_length=48)
    connector_id: str = Field(..., max_length=36)
    connector_standard: Optional[ConnectorType] = None
    connector_format: Optional[ConnectorFormat] = None 
    connector_power_type: Optional[PowerType] = None

class CDR(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    id: str = Field(..., max_length=39)
    start_date_time: datetime
    end_date_time: datetime
    session_id: Optional[str] = Field(None, max_length=36)
    cdr_token: CdrToken
    auth_method: Optional[AuthMethod] = None  # This should be an Enum if defined
    authorization_reference: Optional[str] = Field(None, max_length=36)
    cdr_location: CdrLocation  # Assuming CdrLocation is a custom type
    meter_id: Optional[str] = Field(None, max_length=255)
    currency: str = Field(..., max_length=3)
    tariffs: Optional[List[Tariff]] = Field(default_factory=list)  # Assuming Tariff is a custom type
    charging_periods: Optional[List[ChargingPeriod]] = Field(default_factory=list)  # Assuming ChargingPeriod is a custom type
    signed_data: Optional[SignedData] = None  # Assuming SignedData is a custom type
    total_cost: Optional[Price] = None  # Assuming Price is a custom type
    total_fixed_cost: Optional[Price] = None
    total_energy: Optional[float] = None
    total_energy_cost: Optional[Price] = None
    total_time: Optional[float] = None
    total_time_cost: Optional[Price] = None
    total_parking_time: Optional[float] = None
    total_parking_cost: Optional[Price] = None
    total_reservation_cost: Optional[Price] = None
    remark: Optional[str] = Field(None, max_length=255)
    invoice_reference_id: Optional[str] = Field(None, max_length=39)
    credit: Optional[bool] = None
    credit_reference_id: Optional[str] = Field(None, max_length=39)
    home_charging_compensation: Optional[bool] = None
    last_updated: datetime