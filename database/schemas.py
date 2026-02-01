from typing import List, Optional
from pydantic import BaseModel


# Representa o modelo de perfil associado ao estudante. from_attributes permite criar esse schema a partir de objetos ORM (SQLAlchemy).
class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str

    class Config:
        from_attributes = True


# Modelo usado para criação de um perfil, o banco gera o id automaticamente
class PerfilCreate(BaseModel):
    idade: int
    endereco: str


# Modleo de SAÍDA de estudante com objeto Estudante convertido de ORM para JSON.
class Estudante(BaseModel):
    id: int
    nome: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True


# Modelo de ENTRADA para criar estudante
class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate


# Modelo de SAÍDA de disciplina
class Disciplina(BaseModel):
    id: int
    nome: str
    descricao: str


# Modelo de ENTRADA para criar disciplina
class DisciplinaCreate(BaseModel):
    nome: str
    descricao: str


# Modelo de SAÍDA para matrícula, representa o vínculo entre estudante e disciplina usando seus ids
class Matricula(BaseModel):
    estudante_id: int
    disciplina_id: int

    class Config:
        from_attributes = True


# Modelo de ENTRADA para criar uma matrícula.
class MatriculaCreate(BaseModel):
    estudante_id: int
    disciplina_id: int


# Modelo de SAÍDA de professor
class Professor(BaseModel):
    nome: str

    class Config:
        from_attributes = True


# Modelo de ENTRADA para criar professor.
class ProfessorCreate(BaseModel):
    nome: str
