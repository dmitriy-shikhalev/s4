from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_CONNECTION_STRING: str = "sqlite:///test.db"
