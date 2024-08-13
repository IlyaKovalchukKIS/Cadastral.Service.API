import aiohttp


async def post_aiohttp(url, data: dict | None = None):
    """
    Функция отправки запроса на сервер
    :param url: url сервера
    :param data: данные для отправки на сервер
    :return: ответ сервера
    """
    async with aiohttp.ClientSession() as session_aiohttp:
        async with session_aiohttp.post(url=url, params=data) as response:
            response_server = await response.json()
            return response_server
