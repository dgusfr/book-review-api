from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from database.error_schemas import ErrorResponse


def validation_exception_handler(request: Request, exc: RequestValidationError):
    payload = ErrorResponse(
        code="validation_error",
        message="Dados inválidos",
        details=exc.errors(),
    ).model_dump()
    return JSONResponse(status_code=422, content=payload)
