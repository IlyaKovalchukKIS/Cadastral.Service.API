from datetime import datetime

from pydantic import BaseModel


class CadasterCreate(BaseModel):
    cadaster_number: str
    longitude: str
    width: str


class CadasterRead(CadasterCreate):
    id: int
    date_at: datetime
    result: bool
