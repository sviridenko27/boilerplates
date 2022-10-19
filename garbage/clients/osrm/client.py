from typing import Optional, List, Type

from shapely.geometry import Point, LineString

from garbage.clients.http.client import HTTPClient, HTTPClientType
from garbage.clients.osrm.base import AbstractOSRMService
from garbage.clients.osrm.models import Versions, Profile, Services
from garbage.configuration.settings import settings


class OSRMService(AbstractOSRMService):

    def __init__(
        self,
        base_url: str = settings.OSRM_BASE_URL,
        base_headers: Optional[dict] = None,
        request_timeout: int = settings.OSRM_DEFAULT_REQUEST_TIMEOUT,
        client: Type[HTTPClientType] = HTTPClient,
        api_version: str = Versions.V1,
    ):
        self.http = client(base_url, request_timeout, base_headers)
        self.api_version = api_version

    def get_shortest_path(self, source: Point, destination: Point) -> LineString:
        """
        Returning path LineString between two points.
        """
        route = self.get_route(source, destination)
        return LineString(route['routes'][0]['geometry']['coordinates'])

    def get_route(
        self,
        source: Point,
        destination: Point,
        transportation_mode: Profile = Profile.CAR,
        alternatives: bool = False,
        steps: bool = False,
        annotations: bool = False,
        geometries: str = 'geojson',
        overview: str = 'simplified',
        headers: Optional[dict] = None,
    ) -> dict:
        """
        geometries: polyline, polyline6, geojson
        overview: simplified, full, false
        """
        coordinates = self._coordinates_to_uri_attribute([source, destination])
        uri = self.http._urijoin((Services.ROUTE.value, Versions.V1.value, transportation_mode.value, coordinates))
        params = {
            'alternatives': self._serialize_bool(alternatives),
            'steps': self._serialize_bool(steps),
            'annotations': self._serialize_bool(annotations),
            'geometries': geometries,
            'overview': overview,
        }

        response = self.http.request(method='GET', uri=uri, params=params, headers=headers)
        response_data = response.json()

        return response_data

    @staticmethod
    def _serialize_bool(value: bool) -> str:
        return 'true' if value else 'false'

    @staticmethod
    def _coordinates_to_uri_attribute(coordinates: List[Point]):
        return ';'.join(f'{coordinate.x},{coordinate.y}' for coordinate in coordinates)
