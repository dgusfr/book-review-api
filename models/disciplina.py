from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.database import Base


class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    matriculas = relationship(
        "Matricula",
        back_populates="disciplina",
        cascade="all, delete-orphan",
    )
