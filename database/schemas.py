from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True


class PerfilCreate(BaseModel):
    idade: int
    endereco: str


class Estudante(BaseModel):
    id: int
    nome: str
    email: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True


class EstudanteCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: PerfilCreate


class Disciplina(BaseModel):
    id: int
    nome: str
    descricao: str

    class Config:
        from_attributes = True


class DisciplinaCreate(BaseModel):
    nome: str
    descricao: str


class Matricula(BaseModel):
    estudante_id: int
    disciplina_id: int

    class Config:
        from_attributes = True


class MatriculaCreate(BaseModel):
    estudante_id: int
    disciplina_id: int


class Professor(BaseModel):
    nome: str

    class Config:
        from_attributes = True


class ProfessorCreate(BaseModel):
    nome: str
