from typing import Optional
from domains.pydantic.objects.parkit.tokensTypesFuture import Token
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime

class CancelReservation(BaseModel):
    response_url: str  # Assuming URL type is represented as a string
    reservation_id: str = Field(..., max_length=36)

class ReserveNow(BaseModel):
    response_url: str  # Assuming URL type is represented as a string
    token: Token  # Assuming Token is a custom class
    expiry_date: datetime
    reservation_id: str = Field(..., max_length=36)
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    authorization_reference: Optional[str] = Field(None, max_length=36)

class UnlockConnector(BaseModel):
    response_url: str  # Assuming URL is a string
    location_id: str = Field(..., max_length=36)
    evse_uid: str = Field(..., max_length=36)
    connector_id: str = Field(..., max_length=36)