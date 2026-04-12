from abc import ABC
from typing import Optional
from urllib.parse import urljoin


class AbstractHTTPClient(ABC):
    # TODO: добавить exceptions
    # TODO: добавить имплементацию с авторизацией
    # TODO: добавить сигнатуру для cookies

    BASE_URL: str
    GENERAL_HEADERS: dict
    COOKIES: dict
    REQUEST_TIMEOUT: int = 60

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

    def _urijoin(self, uri_parts: tuple[str]) -> str:
        return '/'.join(uri_parts)
