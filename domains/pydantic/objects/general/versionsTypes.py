from typing import List, Optional, Union
from pydantic import BaseModel, Field, HttpUrl # type: ignore
from datetime import datetime, time
from enum import Enum

class InterfaceRole(str, Enum):
    SENDER = "SENDER"
    RECEIVER = "RECEIVER"

class Endpoint(BaseModel):
    identifier: str
    role: InterfaceRole
    url: str



class VersionNumber(str, Enum):
    v2_0 = "2.0"
    v2_1 = "2.1"
    v2_1_1 = "2.1.1"
    v2_2 = "2.2"
    v2_2_1 = "2.2.1"

class Version(BaseModel):
    version: VersionNumber
    url: str


