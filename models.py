from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


# Esta classe a baixo representa a tabela de estudantes e define as colunas básicas (id, nome, email) e as relações 1:1 (Perfil), 1:N (Matrícula) e N:1 (Professor).
class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)  # Chave primária do estudante
    nome = Column(String)
    email = Column(String)

    perfil = relationship(
        "Perfil",
        back_populates="estudante",
        uselist=False,  # Garante relação 1:1 (um estudante tem um único perfil)
        cascade="all, delete-orphan",  # Ao apagar o estudante, apaga também o perfil ligado a ele
    )

    matriculas = relationship(
        "Matricula",
        back_populates="estudante",
        cascade="all, delete-orphan",  # Ao apagar o estudante, apaga todas as matrículas dele
    )

    professor_id = Column(
        Integer, ForeignKey("professores.id")
    )  # Chave estrangeira para Professor
    professor = relationship(
        "Professor",
        back_populates="estudantes",  # Liga o estudante ao professor responsável (muitos para um)
    )


# Esta classe representa o perfil do estudante, com detalhes adicionais como idade e endereço, e mantém a relação 1:1 com Estudante.
class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)

    estudante_id = Column(
        Integer,
        ForeignKey("estudantes.id"),
        unique=True,  # Garante que um perfil pertence a apenas um estudante (reforça 1:1)
    )

    estudante = relationship(
        "Estudante",
        back_populates="perfil",  # Lado inverso da relação 1:1 com Estudante
    )


# Esta classe representa a tabela de disciplinas, com colunas para id, nome e descrição, e mantém a relação 1:N com Matricula.
class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    matriculas = relationship(
        "Matricula",
        back_populates="disciplina",
        cascade="all, delete-orphan",  # Ao apagar a disciplina, remove as matrículas ligadas a ela
    )


# Esta classe representa a tabela de matrículas, ligando estudantes e disciplinas através de chaves estrangeiras.
class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)

    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    estudante = relationship(
        "Estudante",
        back_populates="matriculas",  # Lado N da relação estudante–matrículas
    )

    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    disciplina = relationship(
        "Disciplina",
        back_populates="matriculas",  # Lado N da relação disciplina–matrículas
    )


# Esta classe representa a tabela de professores, com colunas para id e nome, e mantém a relação 1:N com Estudante.
class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    estudantes = relationship(
        "Estudante",
        back_populates="professor",
        cascade="all, delete-orphan",  # Ao apagar o professor, remove os estudantes associados (cuidado com isso!)
    )
