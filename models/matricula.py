from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)

    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    estudante = relationship(
        "Estudante",
        back_populates="matriculas",
    )

    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    disciplina = relationship(
        "Disciplina",
        back_populates="matriculas",
    )
