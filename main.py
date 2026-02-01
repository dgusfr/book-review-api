from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

# Cria as tabelas no banco com base nos modelos.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependência para fornecer uma sessão do banco por requisição, garantindo o fechamento.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Cria uma nova matrícula e salva no banco, retornando a matrícula criada.
@app.post("/matriculas/", response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@app.get("/matriculas/", response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()
