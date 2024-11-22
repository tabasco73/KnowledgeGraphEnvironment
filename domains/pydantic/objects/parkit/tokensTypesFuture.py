from enum import Enum
from pydantic import BaseModel, Field # type: ignore
from typing import Optional

from domains.pydantic.objects.general.generalTypes import DisplayText
from domains.pydantic.objects.parkit.tokensTypes import Token

class LocationReferences(BaseModel):
    location_id: str = Field(..., max_length=36)
    evse_uid: str = Field(..., max_length=36)

class AllowedType(str, Enum):
    ALLOWED = "ALLOWED"
    BLOCKED = "BLOCKED"
    EXPIRED = "EXPIRED"
    NO_CREDIT = "NO_CREDIT"
    NOT_ALLOWED = "NOT_ALLOWED"

class AuthorizationInfo(BaseModel):
    allowed: AllowedType
    token: Token
    location: Optional[LocationReferences] = None
    authorization_reference: Optional[str] = Field(None, max_length=36)
    info: Optional[DisplayText] = None