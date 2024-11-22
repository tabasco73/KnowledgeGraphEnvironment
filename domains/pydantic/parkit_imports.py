from domains.pydantic.objects.general.credentialsTypes import Credentials, CredentialsRole
from domains.pydantic.objects.general.generalTypes import DisplayText, Price, Role
from domains.pydantic.objects.general.locationsRootTypes import BusinessDetails, ConnectorFormat,ConnectorType, GeoLocation, Image, ImageCategory, PowerType
from domains.pydantic.objects.general.messageVersionsTypes import GetSupportedVersionRequest, GetSupportedVersionsResponse, GetVersionDetailRequest, GetVersionDetailsResponse
from domains.pydantic.objects.parkit.tokensRootTypes import TokenType
from domains.pydantic.objects.general.versionsTypes import Endpoint, InterfaceRole, Version, VersionNumber
from domains.pydantic.objects.parkit.cDRsRootTypes import AuthMethod, CdrDimension, CdrDimensionType, CdrToken, ChargingPeriod
from domains.pydantic.objects.parkit.cDRsTypes import CDR, CdrLocation, SignedData, SignedValue
from domains.pydantic.objects.parkit.commandsTypes import CommandResponse, CommandResultType, CommandResponseType,  CommandResult, CommandType, StartSession, StopSession
from domains.pydantic.objects.parkit.messageCDRsTypes import GetCDRsSenderRequest, GetCDRsSenderResponse, GetCDRsReceiverResponse, GetCDRsReceiverRequest, PostCDRsReceiverRequest, PostCDRsReceiverResponse
from domains.pydantic.objects.parkit.messageCommandsTypes import PostCommandSenderRequestParams, PostCommandSenderRequestBody, PostCommandSenderResponse, PostCommandReceiverRequestBody, PostCommandReceiverResponse
from domains.pydantic.objects.parkit.sessionsTypes import ProfileType
from domains.pydantic.objects.parkit.tariffsRootTypes import PriceComponent, ReservationRestrictionType, Tariff, TariffDimensionType, TariffElement, TariffType
from domains.pydantic.objects.parkit.tokensTypes import EnergyContract, WhitelistType, Token
from domains.pydantic.objects.general.messageCredentialsTypes import GetCredentialsResponse, PostCredentialsResponse, PostCredentialsRequest, PutCredentialsResponse, PutCredentialsRequest
from domains.pydantic.objects.parkit.messageTokensTypes import  GetTokensReceiverRequest, GetTokensReceiverResponse, PutTokensReceiverRequestBody, PutTokensRecieverRequestParams, PatchTokensReceiverRequest, GetTokensSenderRequest, GetTokensSenderResponse, PostTokensSenderRequestParams, PostTokensSenderRequestBody, PostTokensSenderResponse
from domains.pydantic.objects.ecoMovement.locationsTypes import PublishTokenType, AdditionalGeoLocation, Status, StatusSchedule, Capability, ParkingRestriction, RegularHours, ExceptionalPeriod, Hours, EnergySourceCategory, EnergySource, EnvironmentalImpactCategory, EnvironmentalImpact, EnergyMix, ParkingType, Facility, Connector, EVSE, Location
from domains.pydantic.objects.ecoMovement.messageLocationsTypes import GetLocationsSenderRequestList, GetLocationsSenderResponseList, GetLocationsSenderRequestObject, GetLocationsSenderResponseObject, GetLocationsReceiverRequest, GetLocationsReceiverResponse, PutLocationsReceiverRequest, PutLocationsReceiverResponse, PatchLocationsReceiverRequest, PatchLocationsReceiverResponse

all_classes = [CredentialsRole, Credentials, 
    Role, Price, DisplayText,
    ConnectorFormat, ConnectorType, PowerType, GeoLocation, ImageCategory, Image, BusinessDetails,
    GetCredentialsResponse, PostCredentialsResponse, PostCredentialsRequest, PutCredentialsResponse, PutCredentialsRequest,
    GetSupportedVersionRequest, GetSupportedVersionsResponse, GetVersionDetailRequest, GetVersionDetailsResponse,
    TokenType,
    Endpoint, Version, InterfaceRole, VersionNumber,
    CdrDimensionType, CdrDimension, ChargingPeriod, AuthMethod, CdrToken,
    SignedValue, SignedData, CdrLocation, CDR,
    CommandResultType, CommandResponseType, CommandResponse, CommandResult, CommandType, StartSession, StopSession,
    GetCDRsSenderRequest, GetCDRsSenderResponse, GetCDRsReceiverResponse, GetCDRsReceiverRequest, PostCDRsReceiverRequest, PostCDRsReceiverResponse, 
    PostCommandSenderRequestParams, PostCommandSenderRequestBody, PostCommandSenderResponse, PostCommandReceiverRequestBody, PostCommandReceiverResponse,
    ProfileType, 
    GetTokensReceiverRequest, GetTokensReceiverResponse, PutTokensReceiverRequestBody, PutTokensRecieverRequestParams, PatchTokensReceiverRequest, GetTokensSenderRequest, GetTokensSenderResponse, PostTokensSenderRequestParams, PostTokensSenderRequestBody, PostTokensSenderResponse,
    ReservationRestrictionType, TariffDimensionType, PriceComponent, TariffType, TariffElement, Tariff,
    EnergyContract, WhitelistType, Token,
    PublishTokenType, AdditionalGeoLocation, Status, StatusSchedule, Capability, ParkingRestriction, RegularHours, ExceptionalPeriod, Hours, EnergySourceCategory, EnergySource, EnvironmentalImpactCategory, EnvironmentalImpact, EnergyMix, ParkingType, Facility, Connector, EVSE, Location,
    GetLocationsSenderRequestList, GetLocationsSenderResponseList, GetLocationsSenderRequestObject, GetLocationsSenderResponseObject, GetLocationsReceiverRequest, GetLocationsReceiverResponse, PutLocationsReceiverRequest, PutLocationsReceiverResponse, PatchLocationsReceiverRequest, PatchLocationsReceiverResponse
    ]

not_messages = [PostTokensSenderRequestParams, PostTokensSenderRequestBody, GetTokensSenderRequest,GetTokensSenderResponse, PostTokensSenderResponse,
                
                GetLocationsReceiverRequest, PutLocationsReceiverRequest,  PatchLocationsReceiverRequest, 
                GetLocationsReceiverResponse, PutLocationsReceiverResponse, PatchLocationsReceiverResponse,
                PostCommandSenderRequestParams, PostCommandSenderRequestBody, PostCommandSenderResponse,
                GetCDRsReceiverRequest, GetCDRsReceiverResponse, PostCDRsReceiverRequest, PostCDRsReceiverResponse,
                GetTokensSenderRequest, GetTokensSenderResponse, PostTokensSenderRequestParams, PostTokensSenderRequestBody, PostTokensSenderResponse,  
                ]
not_objs = [StopSession]

messages = [
    # Credentials All OCPI 2.2.1 actors
    GetCredentialsResponse, PostCredentialsResponse, PostCredentialsRequest, PutCredentialsResponse, PutCredentialsRequest,
    # Versions All of them
    GetSupportedVersionRequest, GetSupportedVersionsResponse, GetVersionDetailRequest, GetVersionDetailsResponse,

    # Locations

    # CPO will send and eMSP will receive
    GetLocationsSenderResponseList, GetLocationsSenderResponseObject, 
    
    # CPO will receive and eMSP will send
    GetLocationsSenderRequestList, GetLocationsSenderRequestObject,
    
    # Commands

    # CPO will send and eMSP will receive
    PostCommandReceiverRequestBody,
    # CPO will receive and eMSP will send
    PostCommandReceiverResponse,

    # CDRs

    # CPO will send and eMSP will receive
    GetCDRsSenderResponse,
    # CPO will receive and eMSP will send
    GetCDRsSenderRequest,

    # Tokens

    # CPO will send and eMSP will receive
    GetTokensReceiverResponse,
    # CPO will receive and eMSP will send
    GetTokensReceiverRequest, PutTokensReceiverRequestBody, PutTokensRecieverRequestParams, PatchTokensReceiverRequest,
    # Sessions
]

classes_list = [class_ for class_ in all_classes if class_ not in not_messages + not_objs]