from pydantic import BaseModel # type: ignore
from typing import List, Optional
from datetime import datetime

from domains.pydantic.objects.parkit.cDRsTypes import CDR

"""Sender Interface - CPO Implements"""

# GET

class GetCDRsSenderRequest(BaseModel):
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    offset: Optional[int] = 0
    limit: Optional[int] = 100

class GetCDRsSenderResponse(BaseModel):
    CDR: List[CDR] 

"""Receiver Interface - eMSP Implements"""

# GET

class GetCDRsReceiverRequest(BaseModel):
    """ This is up to eMSP to decide, OCPI 2.2.1 does not enforce this."""
    cdr_id: str

class GetCDRsReceiverResponse(BaseModel):
    CDR: CDR

# POST

class PostCDRsReceiverRequest(BaseModel):
    CDR: CDR

class PostCDRsReceiverResponse(BaseModel):
    Location: str