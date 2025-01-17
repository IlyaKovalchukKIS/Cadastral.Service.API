import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_ECHO: bool = os.getenv("DB_ECHO")
    SERVER_URL: str = 'http://server:8001/status/code'
    DB_HOST: str = 'db'

    @property
    def DB_URI_async(self):
        return f'postgresql+asyncpg://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:5432/postgres'


config = Config()
