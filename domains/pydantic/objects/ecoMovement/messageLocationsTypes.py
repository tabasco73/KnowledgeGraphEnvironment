from domains.pydantic.objects.ecoMovement.locationsTypes import EVSE, Connector, Location, Status
from pydantic import BaseModel, Field # type: ignore
from typing import List, Optional, Union
from datetime import datetime

"""Sender Interface - CPO Implements"""

# GET

class GetLocationsSenderRequestList(BaseModel):
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    offset: Optional[int] = Field(0)
    limit: Optional[int] = Field(100)

class GetLocationsSenderResponseList(BaseModel):
    data: List[Location]

class GetLocationsSenderRequestObject(BaseModel):
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)

class GetLocationsSenderResponseObject(BaseModel):
    data: Union[Location, EVSE, Connector]

"""Receiver Interface - eMSP Implements"""

# GET

class GetLocationsReceiverRequest(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)

class GetLocationsReceiverResponse(BaseModel):
    response: Union[Location, EVSE, Connector]

# PUT

class PutLocationsReceiverRequest(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)

class PutLocationsReceiverResponse(BaseModel):
    request_body: Union[Location, EVSE, Connector]

# PATCH

class PatchLocationsReceiverRequest(BaseModel):
    country_code: str = Field(..., max_length=2)
    party_id: str = Field(..., max_length=3)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)

class PatchLocationsReceiverResponse(BaseModel):
    status: Optional[Status] = None
    name: Optional[str] = None
    tariff_ids: Optional[List[str]] = None
    last_updated: datetime = Field(...)