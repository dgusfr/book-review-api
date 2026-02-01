from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Perfil(Base):
    __tablename__ = "perfis"

    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)

    estudante_id = Column(Integer, ForeignKey("estudantes.id"), unique=True)

    estudante = relationship(
        "Estudante",
        back_populates="perfil",
    )
