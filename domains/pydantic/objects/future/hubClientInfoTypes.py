from enum import Enum
from domains.pydantic.objects.general.generalTypes import Role
from pydantic import BaseModel, Field # type: ignore
from datetime import datetime

class ConnectionStatus(str, Enum):
    CONNECTED = "CONNECTED"
    OFFLINE = "OFFLINE"
    PLANNED = "PLANNED"
    SUSPENDED = "SUSPENDED"

class ClientInfo(BaseModel):
    party_id: str = Field(..., max_length=3)
    country_code: str = Field(..., max_length=3)
    role: Role  # Assuming Role is a custom enum or class
    status: ConnectionStatus  # Assuming ConnectionStatus is a custom enum
    last_updated: datetime