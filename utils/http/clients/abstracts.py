from abc import ABC
from typing import Optional
from urllib.parse import urljoin


class AbstractHTTPClient(ABC):
    # TODO: добавить exceptions
    # TODO: добавить имплементацию с авторизацией

    def __init__(self, base_url: str, request_timeout: int = 60, headers: Optional[dict] = None):
        self.url = base_url
        self.request_timeout = request_timeout
        self.__headers = headers or {}

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        files: Optional[dict] = None,
    ):
        raise NotImplementedError

    def _urljoin(self, url: str, uri: str) -> str:
        return urljoin(url, uri)

    def _headersjoin(self, headers, extend_headers: Optional[dict]) -> dict:
        return {**headers, **extend_headers}

    def _urijoin(self, uri_parts: tuple[str]) -> str:
        return '/'.join(uri_parts)
