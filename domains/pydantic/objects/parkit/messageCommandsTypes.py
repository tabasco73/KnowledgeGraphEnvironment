from domains.pydantic.objects.future.commandsTypesFuture import CancelReservation, ReserveNow, UnlockConnector
from domains.pydantic.objects.parkit.commandsTypes import CommandType, StartSession, StopSession, CommandResponse, CommandResult
from pydantic import BaseModel, Field # type: ignore
from typing import Optional, Union

"""Sender Interface - eMSP Implements"""

# POST

class PostCommandSenderRequestParams(BaseModel):
    command: CommandType

class PostCommandSenderRequestBody(BaseModel):
    command_object: Union[
        CancelReservation, 
        ReserveNow, 
        StartSession, 
        StopSession, 
        UnlockConnector
    ]

class PostCommandSenderResponse(BaseModel):
    CommandResponse: CommandResponse

"""Receiver Interface - CPO Implements"""

# POST

class PostCommandReceiverRequestBody(BaseModel):
    CommandResult: CommandResult

class PostCommandReceiverResponse(BaseModel):
    """ This is up to eMSP to decide, OCPI 2.2.1 does not enforce this."""
    command: CommandType
    uid: str

