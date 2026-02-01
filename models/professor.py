from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.database import Base


class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    estudantes = relationship(
        "Estudante",
        back_populates="professor",
        cascade="all, delete-orphan",  # mantém como você já tinha (mas é perigoso em prod)
    )
