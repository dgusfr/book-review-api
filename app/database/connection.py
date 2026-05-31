"""Database connection and metadata."""

from pathlib import Path

import databases
from sqlalchemy import MetaData, create_engine

# Caminho do banco (raiz do projeto)
BASE_DIR = Path(__file__).resolve().parents[1]
SQLITE_FILE = BASE_DIR / "app.db"
DATABASE_URL = f"sqlite:///{SQLITE_FILE}"

# Conexão assíncrona
database = databases.Database(DATABASE_URL)

# Metadata para as tabelas
metadata = MetaData()

# Engine síncrono para criar tabelas
engine = create_engine(DATABASE_URL)


def create_tables():
    """Criar todas as tabelas definidas no metadata."""
    metadata.create_all(engine)
