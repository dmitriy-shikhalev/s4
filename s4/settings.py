from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING: str = "postgresql://postgres:changeme@localhost:5432/s4"
