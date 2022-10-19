from enum import Enum


class Profile(Enum):
    CAR: str = 'car'
    BIKE: str = 'bike'
    FOOT: str = 'foot'


class Versions(Enum):
    V1: str = 'v1'


class Services(Enum):
    ROUTE: str = 'route'
