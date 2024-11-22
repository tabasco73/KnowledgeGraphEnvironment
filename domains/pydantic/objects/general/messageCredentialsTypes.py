from domains.pydantic.objects.general.credentialsTypes import Credentials
from pydantic import BaseModel # type: ignore

""" All OCPI 2.2.1 actors"""

# GET

class GetCredentialsResponse(BaseModel):
    credentials: Credentials

# POST

class PostCredentialsRequest(BaseModel):
    credentials: Credentials

class PostCredentialsResponse(BaseModel):
    credentials: Credentials

# PUT

class PutCredentialsRequest(BaseModel):
    credentials: Credentials

class PutCredentialsResponse(BaseModel):
    credentials: Credentials
