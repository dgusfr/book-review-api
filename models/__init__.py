from database.database import Base

from .estudante import Estudante
from .perfil import Perfil
from .disciplina import Disciplina
from .matricula import Matricula
from .professor import Professor

__all__ = [
    "Base",
    "Estudante",
    "Perfil",
    "Disciplina",
    "Matricula",
    "Professor",
]
