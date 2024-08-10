from src.repository.models import Cadaster


async def create_cadaster(session, data_in, response_server):
    data = data_in.model_dump()
    data['result'] = response_server
    cadaster = Cadaster(**data)
    session.add(cadaster)
    await session.commit()
    await session.refresh(cadaster)
    return cadaster
