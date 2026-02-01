from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from database.database import get_db
import models
import schemas

router = APIRouter()


@router.get("/disciplinas/", response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(models.Disciplina).all()


@router.post("/disciplinas/", response_model=schemas.Disciplina)
def criar_disciplina(
    disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)
):
    db_disciplina = models.Disciplina(**disciplina.model_dump())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina
