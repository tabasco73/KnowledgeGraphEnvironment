from typing import List
from domains.pydantic.objects.general.generalTypes import Role
from domains.pydantic.objects.general.locationsRootTypes import BusinessDetails
from pydantic import BaseModel # type: ignore

class CredentialsRole(BaseModel):
    role: Role
    business_details: BusinessDetails
    party_id: str
    country_code: str
    
class Credentials(BaseModel):
    token: str
    url: str
    roles: List[CredentialsRole]