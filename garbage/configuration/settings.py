from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):

    # Clients settings
    HTTP_DEFAULT_REQUEST_TIMEOUT: int = 30

    OSRM_DEFAULT_REQUEST_TIMEOUT: int = 30
    OSRM_BASE_URL: AnyUrl = 'http://127.0.0.1:5000/'

    EGTS_DEFAULT_REQUEST_TIMEOUT: int = 30
    EGTS_BASE_URL: AnyUrl = 'http://127.0.0.1/ServiceJSON/'
    EGTS_SERVICE_LOGIN: str = ''
    EGTS_SERVICE_PASSWORD: str = ''

    class Config:
        env_file = '.environment'


settings = Settings()
