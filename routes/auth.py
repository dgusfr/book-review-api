from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
from database.database import get_db
from database import schemas
from security import create_access_token, verify_password
from typing import cast

router = APIRouter(tags=["auth"])


@router.post("/token", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = (
        db.query(models.Estudante)
        .filter(models.Estudante.email == form_data.username)
        .first()
    )
    if not user or not verify_password(form_data.password, cast(str, user.senha_hash)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    token = create_access_token(subject=cast(str, user.email))
    return {"access_token": token, "token_type": "bearer"}
