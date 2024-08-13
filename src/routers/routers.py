from typing import Annotated, List

import fastapi
import aiohttp
from fastapi import Depends
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.repository.crud import create_cadaster, get_history
from src.repository.database import db_helper
from src.schemas.cadastral import CadasterCreate, CadasterSave, CadasterRead
from src.utils import post_aiohttp

api_router = fastapi.APIRouter()


@api_router.post("/query", response_model=CadasterSave)
async def get_query(
        data: CadasterCreate = Depends(),
):
    """Получения запроса по кадастровому номеру, долготе и широте"""
    response = await post_aiohttp(config.SERVER_URL, data.model_dump())
    data = data.model_dump()
    data['result'] = response
    return data


@api_router.post('/result', response_model=CadasterRead)
async def post_result(
        data: CadasterSave,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Отправка результатов в базу данных по кадастровому номеру, долготе и широте"""
    result = await create_cadaster(session, data)
    return result


@api_router.get('/ping')
async def ping_server():
    """Проверка работоспособности сервера"""
    response = await post_aiohttp('http://server:8001/ping')
    return response


@api_router.get('/history', response_model=List[CadasterRead])
async def get_history_endpoint(session: AsyncSession = Depends(db_helper.session_dependency)):
    """Получение истории запросов на сервер"""
    return await get_history(session)
