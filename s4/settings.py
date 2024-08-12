from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING: str = "postgresql://postgres:changeme@localhost:5433/s4"
    HOST: str = '127.0.0.1'
    PORT: int = 8000
