from typing import Annotated

import fastapi
import aiohttp
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.repository.crud import create_cadaster
from src.repository.database import db_helper
from src.schemas.cadastral import CadasterCreate, CadasterSave

api_router = fastapi.APIRouter()


@api_router.post("/query", response_model=CadasterSave)
async def get_query(
        data: CadasterCreate = Depends(),
):
    async with aiohttp.ClientSession() as session_aiohttp:
        async with session_aiohttp.post(url=config.SERVER_URL, params=data.model_dump()) as response:
            response_server = await response.json()
            data = data.model_dump()
            data['result'] = response_server
            return data


@api_router.post('/result')
async def post_result(
        data: CadasterSave,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    result = await create_cadaster(session, data)
    return {'status': 'Success'}


@api_router.get('/ping')
async def ping_server():
    async with aiohttp.ClientSession() as session_aiohttp:
        async with session_aiohttp.post(url='http://server:8001/ping') as response:
            response_server = await response.json()
            return response_server


@api_router.get('/history')
async def get_history(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await get_history(session)
