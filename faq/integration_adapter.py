import dataclasses
from typing import Any


@dataclasses.dataclass
class FlightDTO:
    some_field_1: int
    some_field_2: str
    some_field_3: bool


class ExampleIntegrationAdapter:
    """
    Communication client could be any transport protocol for example HTTP, grpc, socket, etc.

    Firstly suggest implement methods as this class methods, but later it could be aggregation of many handler
    where Adapter will be router.

    '''
        class ExampleIntegrationRouter:

            def __init__(self, communication_client: Any):
                flights = FlightsHandler(communication_client)
                airplanes = AirplanesHandler(communication_client)


        some_integration_http_client = SomeIntegrationHTTPClient(base_url='www.world.ru', cookies=cookies)
        some_integration_router = ExampleIntegrationRouter(some_integration_http_client)

        airplanes: list[AirplanesDTO] = some_integration_router.airplanes.get_all_airplanes()
    '''
    """
    def __init__(self, communication_client: Any):
        self.communication_client = communication_client

    def get_flight(self) -> FlightDTO:
        try:
            response: dict = self.communication_client.request(
                method='GET',
                uri='flights',
            )
            return FlightDTO(
                some_field_1=response.get('some_field_1'),
                some_field_2=response.get('some_field_2'),
                some_field_3=response.get('some_field_3')
            )
        except Exception as e:      # Here we catch some protocol exceptions
            print(e)                # Use our loggers if it necessary



