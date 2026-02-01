from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload

import models
from database.database import get_db
from database import schemas
from security import get_password_hash

router = APIRouter()


@router.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = (
        db.query(models.Estudante).options(joinedload(models.Estudante.perfil)).all()
    )
    return estudantes


@router.post("/estudantes/", response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        senha_hash=get_password_hash(estudante.senha),
        role="estudante",
        perfil=models.Perfil(**estudante.perfil.model_dump()),
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante
