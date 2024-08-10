import asyncio
from typing import Annotated

from fastapi import FastAPI, Depends
import random

from pydantic import BaseModel

app = FastAPI()


class CadasterCreate(BaseModel):
    cadaster_number: str
    longitude: str
    width: str


@app.post('/status/code')
async def status_check(data: Annotated[CadasterCreate, Depends()]):
    print(data.model_dump())
    await asyncio.sleep(random.randint(1, 6))
    return random.choices([True, False])

