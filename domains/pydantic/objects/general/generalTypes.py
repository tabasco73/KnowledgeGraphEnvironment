from pydantic import BaseModel, Field, HttpUrl # type: ignore
from enum import Enum

class DisplayText(BaseModel):
    language: str
    text: str

class Price(BaseModel):
    excl_vat: float
    incl_vat: float

class Role(str, Enum):
    CPO = "CPO"  # Charge Point Operator Role
    EMSP = "EMSP"  # eMobility Service Provider Role
    HUB = "HUB"  # Hub role
    NAP = "NAP"  # National Access Point Role
    NSP = "NSP"  # Navigation Service Provider Role
    OTHER = "OTHER"  # Other role
    SCSP = "SCSP" 