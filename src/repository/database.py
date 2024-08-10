from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import config

engine = create_async_engine(config.DB_URI_async)


class DBHelper:

    def __init__(self, uri: str, echo: bool = False):
        """
        Класс помощник для создания асинхронных сессий
        :param uri: uri базы данных
        :param echo: выводить ли sql запросы
        """
        self.uri = uri
        self.engine = create_async_engine(url=self.uri)
        self.__async_session_maker = async_sessionmaker(bind=self.engine, expire_on_commit=False, autoflush=False)

    async def session_dependency(self):
        """ Создание сессии """
        async with self.__async_session_maker() as session:
            yield session
            await session.close()


db_helper = DBHelper(uri=config.DB_URI_async, echo=config.DB_ECHO)
