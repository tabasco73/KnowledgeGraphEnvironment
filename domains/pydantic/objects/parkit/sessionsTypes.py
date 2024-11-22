from enum import Enum

""" Charging Preferences """

class ProfileType(str, Enum):
    CHEAP = "CHEAP"
    FAST = "FAST"
    GREEN = "GREEN"
    REGULAR = "REGULAR"