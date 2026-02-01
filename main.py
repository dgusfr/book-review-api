from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from error_handlers import validation_exception_handler

import models
from database.database import engine

from routes import auth, estudantes, disciplinas, professores, matriculas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(auth.router)
app.include_router(estudantes.router)
app.include_router(disciplinas.router)
app.include_router(professores.router)
app.include_router(matriculas.router)
