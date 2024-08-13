from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.models import Cadaster


async def create_cadaster(session, data_in):
    data = data_in.model_dump()
    cadaster = Cadaster(**data)
    session.add(cadaster)
    await session.commit()
    await session.refresh(cadaster)
    return cadaster


async def get_history(session: AsyncSession):
    return await session.execute(select(Cadaster))
