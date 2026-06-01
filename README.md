# Book Review API

API REST de reviews de livros usando FastAPI, PostgreSQL, Redis, Celery e SQLModel.

Este projeto foi reorganizado em uma arquitetura inspirada em MVC:

```text
src/
├── controllers/  # endpoints/rotas FastAPI
├── models/       # modelos SQLModel/tabelas do banco
├── views/        # schemas Pydantic de entrada e saída
└── core/         # config, banco, Redis, services, repositories, segurança, mail e tasks
```

## Requisitos

- Python 3.10+
- Poetry
- PostgreSQL
- Redis
- Docker e Docker Compose, opcional mas recomendado

## Configuração local

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

Instale as dependências:

```bash
poetry install
```

Gere o lockfile, caso ele ainda não exista:

```bash
poetry lock
```

Rode as migrations:

```bash
poetry run alembic upgrade head
```

Suba a API:

```bash
poetry run uvicorn src.main:app --reload
```

Acesse:

```text
http://localhost:8000/api/v1/docs
```

## Rodando com Docker

Crie o `.env` a partir do `.env.example` e execute:

```bash
docker compose up --build
```

A API ficará disponível em:

```text
http://localhost:8000/api/v1/docs
```

## Celery

Com Docker, o worker Celery já sobe pelo serviço `celery`.

Localmente, rode:

```bash
poetry run celery -A src.core.tasks.celery_app.c_app worker --loglevel=info
```

## Testes

```bash
poetry run pytest
```

## Observação sobre `poetry.lock`

O `poetry.lock` não foi incluído neste pacote porque ele deve ser gerado de verdade no seu ambiente com:

```bash
poetry lock
```
