from typing import Optional
from pydantic import BaseModel, Field # type: ignore
from enum import Enum

from domains.pydantic.objects.general.generalTypes import DisplayText
from domains.pydantic.objects.parkit.tokensTypes import Token

class CommandResultType(str, Enum):
    ACCEPTED = "ACCEPTED"
    CANCELED_RESERVATION = "CANCELED_RESERVATION"
    EVSE_OCCUPIED = "EVSE_OCCUPIED"
    EVSE_INOPERATIVE = "EVSE_INOPERATIVE"
    FAILED = "FAILED"
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    UNKNOWN_RESERVATION = "UNKNOWN_RESERVATION"

class CommandResponseType(Enum):
    NOT_SUPPORTED = "NOT_SUPPORTED"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"
    UNKNOWN_SESSION = "UNKNOWN_SESSION"

class CommandResponse(BaseModel):
    result: CommandResponseType
    timeout: Optional[int] = None
    message: Optional[DisplayText] = None

class CommandResult(BaseModel):
    result: CommandResultType
    message: Optional[DisplayText] = None

class CommandType(str, Enum):
    CANCEL_RESERVATION = "CANCEL_RESERVATION"
    RESERVE_NOW = "RESERVE_NOW"
    START_SESSION = "START_SESSION"
    STOP_SESSION = "STOP_SESSION"
    UNLOCK_CONNECTOR = "UNLOCK_CONNECTOR"

class StartSession(BaseModel):
    response_url: str
    token: Token
    location_id: str = Field(..., max_length=36)
    evse_uid: Optional[str] = Field(None, max_length=36)
    connector_id: Optional[str] = Field(None, max_length=36)
    authorization_reference: Optional[str] = Field(None, max_length=36)

class StopSession(BaseModel):
    response_url: str
    session_id: str = Field(..., max_length=36)