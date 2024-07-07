from fastapi import FastAPI

from app.container import Container
from.domain_a.endpoint import router as a_router


container = Container()
db = container.db()
# db.create_database()

app = FastAPI()
app.container = container

app.include_router(a_router)
