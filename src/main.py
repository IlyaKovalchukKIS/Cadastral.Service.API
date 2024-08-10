import threading

import uvicorn
from fastapi import FastAPI

from src.routers.routers import api_router

app = FastAPI()
app.include_router(api_router)
