from typing import Protocol, Optional

from requests import Response


class AbstractHTTPClient(Protocol):
    """Base class for implement HTTP usage."""

    @property
    def headers(self) -> dict: ...

    @headers.setter
    def headers(self, headers) -> dict: ...

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> Response:
        ...
