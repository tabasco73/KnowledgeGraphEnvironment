from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl # type: ignore

class ConnectorType(str, Enum):
    CHADEMO = "CHADEMO"
    CHAOJI = "CHAOJI"
    DOMESTIC_A = "DOMESTIC_A"
    DOMESTIC_B = "DOMESTIC_B"
    DOMESTIC_C = "DOMESTIC_C"
    DOMESTIC_D = "DOMESTIC_D"
    DOMESTIC_E = "DOMESTIC_E"
    DOMESTIC_F = "DOMESTIC_F"
    DOMESTIC_G = "DOMESTIC_G"
    DOMESTIC_H = "DOMESTIC_H"
    DOMESTIC_I = "DOMESTIC_I"
    DOMESTIC_J = "DOMESTIC_J"
    DOMESTIC_K = "DOMESTIC_K"
    DOMESTIC_L = "DOMESTIC_L"
    DOMESTIC_M = "DOMESTIC_M"
    DOMESTIC_N = "DOMESTIC_N"
    DOMESTIC_O = "DOMESTIC_O"
    GBT_AC = "GBT_AC"
    GBT_DC = "GBT_DC"
    IEC_60309_2_single_16 = "IEC_60309_2_single_16"
    IEC_60309_2_three_16 = "IEC_60309_2_three_16"
    IEC_60309_2_three_32 = "IEC_60309_2_three_32"
    IEC_60309_2_three_64 = "IEC_60309_2_three_64"
    IEC_62196_T1 = "IEC_62196_T1"
    IEC_62196_T1_COMBO = "IEC_62196_T1_COMBO"
    IEC_62196_T2 = "IEC_62196_T2"
    IEC_62196_T2_COMBO = "IEC_62196_T2_COMBO"
    IEC_62196_T3A = "IEC_62196_T3A"
    IEC_62196_T3C = "IEC_62196_T3C"
    NEMA_5_20 = "NEMA_5_20"
    NEMA_6_30 = "NEMA_6_30"
    NEMA_6_50 = "NEMA_6_50"
    NEMA_10_30 = "NEMA_10_30"
    NEMA_10_50 = "NEMA_10_50"
    NEMA_14_30 = "NEMA_14_30"
    NEMA_14_50 = "NEMA_14_50"
    PANTOGRAPH_BOTTOM_UP = "PANTOGRAPH_BOTTOM_UP"
    PANTOGRAPH_TOP_DOWN = "PANTOGRAPH_TOP_DOWN"
    TESLA_R = "TESLA_R"
    TESLA_S = "TESLA_S"

class PowerType(str, Enum):
    AC_1_PHASE = "AC_1_PHASE"
    AC_2_PHASE = "AC_2_PHASE"
    AC_2_PHASE_SPLIT = "AC_2_PHASE_SPLIT"
    AC_3_PHASE = "AC_3_PHASE"
    DC = "DC"

class ConnectorFormat(str, Enum):
    SOCKET = "SOCKET"
    CABLE = "CABLE"

class GeoLocation(BaseModel):
    latitude: float
    longitude: float

class ImageCategory(str, Enum):
    CHARGER = "CHARGER"
    ENTRANCE = "ENTRANCE"
    LOCATION = "LOCATION"
    NETWORK = "NETWORK"
    OPERATOR = "OPERATOR"
    OTHER = "OTHER"
    OWNER = "OWNER"

class Image(BaseModel):
    url: HttpUrl
    thumbnail: Optional[HttpUrl]
    category: ImageCategory
    type: str
    width: Optional[int]
    height: Optional[int]

class BusinessDetails(BaseModel):
    name: str = Field(..., max_length=100)
    website: Optional[HttpUrl]
    logo: Optional[Image]