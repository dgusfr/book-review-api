from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.schemas.user import UserOut
from src.services.users import list_users

router = APIRouter()


@router.get("/", response_model=List[UserOut])
async def get_users():
    users = await list_users()
    return JSONResponse(content={"users": users})
