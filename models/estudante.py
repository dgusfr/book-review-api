from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)

    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan",
    )

    matriculas = relationship(
        "Matricula",
        back_populates="estudante",
        cascade="all, delete-orphan",
    )

    professor_id = Column(Integer, ForeignKey("professores.id"))
    professor = relationship(
        "Professor",
        back_populates="estudantes",
    )
