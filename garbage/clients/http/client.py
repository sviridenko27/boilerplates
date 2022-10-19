from typing import Optional, Tuple, TypeVar
from urllib.parse import urljoin

import requests
from requests import HTTPError, ConnectionError, Timeout, request, Response

from garbage.clients.http.base import AbstractHTTPClient
from garbage.configuration.settings import settings


class HTTPClient(AbstractHTTPClient):
    HTTP_ERROR_EXCEPTION = HTTPError
    CONNECTION_EXCEPTION = ConnectionError
    TIMEOUT_EXCEPTION = Timeout

    @property
    def headers(self) -> dict:
        return self.__headers

    @headers.setter
    def headers(self, headers: dict) -> None:
        self.__headers = headers

    def __init__(
        self,
        base_url: str,
        request_timeout: int = settings.HTTP_DEFAULT_REQUEST_TIMEOUT,
        general_headers: Optional[dict] = None
    ):
        self.url = base_url
        self.request_timeout = request_timeout
        self.__headers = general_headers or {}

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> Response:
        """
        Base request template with except HTTP exceptions.
        """
        headers = self._headersjoin(self.headers, headers or {})
        url = self._urljoin(self.url, uri)
        try:
            response = request(
                method,
                url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=self.request_timeout
            )
            response.raise_for_status()
        except requests.HTTPError as e:
            raise self.HTTP_ERROR_EXCEPTION from e
        except requests.ConnectionError as e:
            raise self.CONNECTION_EXCEPTION from e
        except requests.Timeout as e:
            raise self.TIMEOUT_EXCEPTION from e

        return response

    def _urljoin(self, url: str, uri: str) -> str:
        return urljoin(url, uri)

    def _headersjoin(self, headers, extend_headers: Optional[dict]) -> dict:
        return {**headers, **extend_headers}

    def _urijoin(self, uri_parts: Tuple[str]) -> str:
        return "/".join(uri_parts)


HTTPClientType = TypeVar('HTTPClientType', bound=HTTPClient)
