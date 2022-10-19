from shapely.geometry import Point


class AbstractOSRMService:
    """
    Provide get requests to OSRM service.

    HTTP implementation description:
    template request: https://{server}/{service}/{version}/{profile}/{coordinates}[.{format}]?option=value&option=value

    API provide access to service which can introduced in Services class
        - route: getting route from point A to point B with additional information.
        - nearest: getting the nearest segment to point.
        - table: computes the duration of the fastest route between all pairs of supplied coordinates.
        - match: correcting GPS marks on graph of segments.
        - trip: solves the Traveling Salesman Problem.
        - tile: generates Mapbox Vector Tiles that can be viewed with a vector-tile.
    """

    def get_route(self, source: Point, destination: Point, *args, **kwargs) -> dict:
        ...
