from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database.database import get_db
import models
import database.schemas as schemas

router = APIRouter()


@router.get("/matriculas/", response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(models.Matricula).all()


@router.post("/matriculas/", response_model=schemas.Matricula)
def criar_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    count_matriculas = (
        db.query(models.Matricula)
        .filter(models.Matricula.estudante_id == matricula.estudante_id)
        .count()
    )
    if count_matriculas >= 5:
        raise HTTPException(
            status_code=400,
            detail="O estudante já possui o número máximo de matrículas permitidas (5).",
        )

    db_matricula = models.Matricula(**matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula
