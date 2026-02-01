from fastapi import FastAPI
import models
from database.database import engine
from routes import estudantes, disciplinas, professores, matriculas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(estudantes.router)
app.include_router(disciplinas.router)
app.include_router(professores.router)
app.include_router(matriculas.router)
