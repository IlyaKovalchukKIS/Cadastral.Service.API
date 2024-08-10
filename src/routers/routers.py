from typing import Annotated

import fastapi
import aiohttp
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.repository.crud import create_cadaster
from src.repository.database import db_helper
from src.schemas.cadastral import CadasterCreate

api_router = fastapi.APIRouter()


@api_router.post("/query")
async def get_query(
        data: Annotated[CadasterCreate, Depends()],
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    async with aiohttp.ClientSession() as session_aiohttp:
        async with session_aiohttp.post(url=config.SERVER_URL, params=data.model_dump()) as response:
            response_server = await response.json()
            await create_cadaster(session=session, data_in=data, response_server=response_server[0])
            return response_server
