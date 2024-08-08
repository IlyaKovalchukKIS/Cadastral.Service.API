import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_PORT: int = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_ECHO: bool = os.getenv("DB_ECHO")

    @staticmethod
    def DB_URI_async():
        return f'postgresql+asyncpg://{Config.DB_USER}:{Config.DB_PASSWORD}@localhost:{Config.DB_PORT}/postgres'


config = Config()
