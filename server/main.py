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


@app.post('/ping')
async def root(data: None = None):
    return {"message": "Server started"}


@app.post('/status/code')
async def status_check(data: Annotated[CadasterCreate, Depends()]):
    await asyncio.sleep(random.randint(1, 60))
    result = random.choices([True, False])
    return result[0]
