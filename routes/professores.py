from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from database.database import get_db
import models
import schemas

router = APIRouter()


@router.get("/professores/", response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(models.Professor).all()


@router.post("/professores/", response_model=schemas.Professor)
def criar_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_professor = models.Professor(**professor.model_dump())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor
