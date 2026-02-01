from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

import models
from database.database import get_db
from database import schemas

router = APIRouter(tags=["estudantes"])


@router.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = (
        db.query(models.Estudante).options(joinedload(models.Estudante.perfil)).all()
    )
    return estudantes


@router.post("/estudantes/", response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    existing = (
        db.query(models.Estudante)
        .filter(models.Estudante.email == estudante.email)
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado",
        )

    db_estudante = models.Estudante(
        nome=estudante.nome,
        email=estudante.email,
        perfil=models.Perfil(**estudante.perfil.model_dump()),
    )

    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)

    return db_estudante
