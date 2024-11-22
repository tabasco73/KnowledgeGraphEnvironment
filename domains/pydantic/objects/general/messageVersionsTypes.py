from domains.pydantic.objects.general.versionsTypes import Endpoint, InterfaceRole, Version, VersionNumber
from pydantic import BaseModel # type: ignore
from typing import List


class GetSupportedVersionRequest(BaseModel):
    """No OCPI 2.2.1 required implementation"""
    version: str
    url: str

class GetSupportedVersionsResponse(BaseModel):
    versions: List[Version]

class GetVersionDetailRequest(BaseModel):
    identifier: str
    role: InterfaceRole
    url: str

class GetVersionDetailsResponse(BaseModel):
    version: VersionNumber
    endpoints: List[Endpoint]