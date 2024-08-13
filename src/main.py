
from fastapi import FastAPI
from sqladmin import Admin

from src.repository.database import db_helper
from src.repository.models import CadasterAdmin
from src.routers.routers import api_router

app = FastAPI()
app.include_router(api_router)
admin = Admin(app, engine=db_helper.engine)
admin.add_view(CadasterAdmin)
