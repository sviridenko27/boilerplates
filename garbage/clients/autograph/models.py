from enum import Enum


class AutographEndpoints(Enum):
    LOGIN = 'Login'
    SCHEMAS = 'EnumSchemas'
    DEVICES = 'EnumDevices'
    TRIP = 'GetTrips'


class AutographEndpointsParams(Enum):
    TOKEN = 'session'
    LOGIN = 'UserName'
    PASSWORD = 'Password'
    SCHEMA = 'schemaID'
    CAR_IDS = 'IDs'
    DATETIME_START = 'SD'
    DATETIME_END = 'ED'
    TRIP_SPLITTER = 'tripSplitterIndex'
