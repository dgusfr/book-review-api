from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from database.database import get_db
from database import schemas
from security import require_admin

router = APIRouter()


@router.get("/disciplinas/", response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(models.Disciplina).all()


@router.post("/disciplinas/", response_model=schemas.Disciplina)
def criar_disciplina(
    disciplina: schemas.DisciplinaCreate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin),
):
    db_disciplina = models.Disciplina(**disciplina.model_dump())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina
