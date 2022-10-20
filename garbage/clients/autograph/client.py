import datetime
from typing import Type, Optional, List

from garbage.clients.autograph.base import AbstractAutographService
from garbage.clients.autograph.models import AutographEndpoints, AutographEndpointsParams
from garbage.clients.http.client import HTTPClientType, HTTPClient
from garbage.configuration.settings import settings


class AutographService(AbstractAutographService):
    """
    This class using for getting additional information for Autograph protocol devices.
    """
    ENDPOINT_URI: AutographEndpoints = AutographEndpoints
    ENDPOINT_PARAMS: AutographEndpointsParams = AutographEndpointsParams

    def __init__(
        self,
        base_url: str = settings.AUTOGRAPH_BASE_URL,
        base_headers: Optional[dict] = None,
        request_timeout: int = settings.AUTOGRAPH_DEFAULT_REQUEST_TIMEOUT,
        client: Type[HTTPClientType] = HTTPClient,
        login: str = settings.AUTOGRAPH_SERVICE_LOGIN,
        password: str = settings.AUTOGRAPH_SERVICE_PASSWORD,
    ):
        self.http = client(base_url, request_timeout, base_headers)
        self.login = login
        self.password = password

    def get_cars_statistic(
        self,
        datetime_start: datetime.datetime,
        datetime_end: datetime.datetime,
        cars: List[dict],
        schema_id: str,
        token: Optional[str] = None,
    ) -> List[dict]:
        cars_trip_statistic = self.get_trip(datetime_start, datetime_end, [car['id'] for car in cars], schema_id, token)

        main_cars_stat = {}
        for car_id, car_trip_stat in cars_trip_statistic.items():
            car_statistic = []

            for trip in car_trip_stat['Trips']:
                for trip_stage in trip['Stages']:

                    trip_stage_items = trip_stage['Items']
                    trip_stage_params: list = trip_stage['Params']

                    fuel_index = trip_stage_params.index('Tank1FuelLevel Last')
                    distance_index = trip_stage_params.index('TotalDistance')
                    datetime_index = trip_stage_params.index('DateTime Last')
                    avg_speed_index = trip_stage_params.index('AverageSpeed')
                    
                    for trip_stage_item in trip_stage_items:
                        values: list = trip_stage_item['Values']
                        car_statistic.append({
                            'fuel_level': values[fuel_index],
                            'distance': values[distance_index],
                            'datetime': values[datetime_index],
                            'avg_speed': values[avg_speed_index],
                        })

            main_cars_stat[car_id] = car_statistic

        cars_statistics = [{**car, 'statistic': main_cars_stat[car['id']]} for car in cars]
        return cars_statistics

    def get_schema_cars_simple(self, schema_id: str, token: Optional[str] = None) -> List[dict]:
        devices = self._get_schema_cars(schema_id, token).get('Items')
        return [{'serial': device.get('Serial'), 'id': device.get('ID')} for device in devices]

    def get_schema_devices_general(self, schema_id: str, token: Optional[str] = None) -> dict:
        return self._get_schema_cars(schema_id, token)

    def get_schemas(self, token: Optional[str] = None) -> List[dict]:
        """
        Getting all car's schemas.
        """
        response = self.http.request(
            method='GET',
            uri=self.ENDPOINT_URI.SCHEMAS.value,
            params={self.ENDPOINT_PARAMS.TOKEN.value: token or self._get_access_token()},
        )

        return response.json()

    def get_trip(
        self,
        datetime_start: datetime.datetime,
        datetime_end: datetime.datetime,
        car_ids: List[str],
        schema_id: str,
        token: Optional[str] = None,
    ) -> dict:
        """
        Getting info about cars trip filtered by datetime.
        """
        response = self.http.request(
            method='GET',
            uri=self.ENDPOINT_URI.TRIP.value,
            params={
                self.ENDPOINT_PARAMS.TOKEN.value: token or self._get_access_token(),
                self.ENDPOINT_PARAMS.SCHEMA.value: schema_id,
                self.ENDPOINT_PARAMS.CAR_IDS.value: self._serialize_multiple_values(car_ids),
                self.ENDPOINT_PARAMS.DATETIME_START.value: self._serialize_datetime(datetime_start),
                self.ENDPOINT_PARAMS.DATETIME_END.value: self._serialize_datetime(datetime_end),
                self.ENDPOINT_PARAMS.TRIP_SPLITTER.value: 0,
            }
        )

        return response.json()

    def _get_access_token(self, login: Optional[str] = None, password: Optional[str] = None) -> str:
        """
        Getting access token for making requests to other API methods.
        """
        response = self.http.request(
            method='GET',
            uri=self.ENDPOINT_URI.LOGIN.value,
            params={
                self.ENDPOINT_PARAMS.LOGIN.value: login or self.login,
                self.ENDPOINT_PARAMS.PASSWORD.value: password or self.password
            },
        )

        return response.text

    def _get_schema_cars(self, schema_id: str, token: Optional[str] = None) -> dict:
        """
        Getting all cars by schema_id.
        """
        response = self.http.request(
            method='GET',
            uri=self.ENDPOINT_URI.DEVICES.value,
            params={
                self.ENDPOINT_PARAMS.TOKEN.value: token or self._get_access_token(),
                self.ENDPOINT_PARAMS.SCHEMA.value: schema_id,
            },
        )

        return response.json()

    @staticmethod
    def _serialize_datetime(value: datetime.datetime, template: Optional[str] = '%Y%m%d-%H%M') -> str:
        return value.strftime(template)

    @staticmethod
    def _serialize_multiple_values(values: List[str]):
        return ','.join(values)
