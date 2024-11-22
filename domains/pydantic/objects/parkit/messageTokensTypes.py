from domains.pydantic.objects.parkit.tokensTypesFuture import AuthorizationInfo, LocationReferences
from pydantic import BaseModel, Field # type: ignore
from typing import List, Optional
from domains.pydantic.objects.parkit.tokensRootTypes import TokenType
from domains.pydantic.objects.parkit.tokensTypes import Token

""" Receiver Interface - CPO Implements """

class GetTokensReceiverRequest(BaseModel):
    country_code: str = Field(..., min_length=2, max_length=2)
    party_id: str = Field(..., min_length=3, max_length=3)
    token_uid: str = Field(..., min_length=36, max_length=36)
    type: Optional[str] = Field("RFID")

class GetTokensReceiverResponse(BaseModel):
    data: Token

class PutTokensReceiverRequestBody(BaseModel):
    data: Token

class PutTokensRecieverRequestParams(BaseModel):
    country_code: str = Field(..., min_length=2, max_length=2)
    party_id: str = Field(..., min_length=3, max_length=3)
    token_uid: str = Field(..., min_length=36, max_length=36)
    type: Optional[str] = TokenType

class PatchTokensReceiverRequest(BaseModel):
    country_code: Optional[str] = Field(None, min_length=2, max_length=2)
    party_id: Optional[str] = Field(None, min_length=3, max_length=3)
    token_uid: Optional[str] = Field(None, min_length=36, max_length=36)
    type: Optional[str] = TokenType
    last_updated: str = Field(...)

""" Sender Interface - eMSP Implements """

class GetTokensSenderRequest(BaseModel):
    date_from: Optional[str] = Field(None)
    date_to: Optional[str] = Field(None)
    offset: Optional[int] = Field(0)
    limit: Optional[int] = Field(None)

class GetTokensSenderResponse(BaseModel):
    data: List[Token]

class PostTokensSenderRequestParams(BaseModel):
    token_uid: str = Field(..., min_length=36, max_length=36)
    type: Optional[str] =TokenType

class PostTokensSenderRequestBody(BaseModel):
    data: Optional[LocationReferences] = Field(None)

class PostTokensSenderResponse(BaseModel):
    data: AuthorizationInfo 