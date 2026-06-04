# Book Review API

API REST para gerenciamento de livros, avaliações e tags, construída com **FastAPI**, **PostgreSQL**, **SQLModel**, **Redis**, **Celery** e **Poetry**.

O projeto foi reorganizado em uma arquitetura inspirada em **MVC**, adaptada para APIs REST:

- **Controllers**: rotas/endpoints FastAPI.
- **Models**: modelos SQLModel e tabelas do banco.
- **Views**: schemas Pydantic usados em requests e responses.
- **Core**: configuração, banco, Redis, autenticação, permissões, services, repositories, e-mail, tasks e middlewares.

---

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Pré-requisitos](#pré-requisitos)
- [Variáveis de ambiente](#variáveis-de-ambiente)
- [Como rodar localmente](#como-rodar-localmente)
- [Como rodar com Docker](#como-rodar-com-docker)
- [Migrations com Alembic](#migrations-com-alembic)
- [Celery e tarefas assíncronas](#celery-e-tarefas-assíncronas)
- [Testes](#testes)
- [Documentação da API](#documentação-da-api)
- [Fluxo de autenticação](#fluxo-de-autenticação)
- [Endpoints principais](#endpoints-principais)
- [Exemplos de payloads](#exemplos-de-payloads)
- [Comandos úteis](#comandos-úteis)
- [Observações importantes](#observações-importantes)

---

## Sobre o projeto

A **Book Review API** é uma API REST para um sistema de avaliação de livros.

Com ela é possível:

- criar conta de usuário;
- autenticar com JWT;
- verificar conta por e-mail;
- renovar token de acesso;
- realizar logout com blocklist em Redis;
- solicitar redefinição de senha;
- cadastrar livros;
- listar livros;
- atualizar livros;
- remover livros;
- criar avaliações de livros;
- listar avaliações;
- remover avaliações;
- criar tags;
- associar tags a livros.

O projeto simula uma API backend mais próxima de um cenário real, com banco relacional, autenticação, background tasks, migrations e organização em camadas.

---

## Tecnologias utilizadas

- **Python**
- **FastAPI**
- **Uvicorn**
- **SQLModel**
- **SQLAlchemy Async**
- **PostgreSQL**
- **AsyncPG**
- **Alembic**
- **Redis**
- **Celery**
- **FastAPI-Mail**
- **PyJWT**
- **Passlib + bcrypt**
- **Pydantic Settings**
- **Poetry**
- **Docker / Docker Compose**
- **Pytest**
- **HTTPX**

---

## Arquitetura do projeto

Este projeto usa uma arquitetura inspirada em **MVC**, adaptada para uma API FastAPI.

### Controllers

Responsáveis por:

- declarar os endpoints;
- receber requests;
- validar dependências;
- chamar services;
- retornar responses.

Exemplo:

```text
request -> controller -> service -> repository -> database
```

---

### Models

Responsáveis por representar as tabelas do banco usando SQLModel.

Principais modelos:

- `User`
- `Book`
- `Review`
- `Tag`
- `BookTag`

---

### Views

Em uma API REST, a camada `views` representa os schemas de entrada e saída.

Responsáveis por:

- validar payloads de entrada;
- definir response models;
- documentar automaticamente os contratos da API no Swagger.

---

### Core

Responsável por partes internas da aplicação:

- configuração;
- conexão com banco;
- Redis;
- autenticação;
- JWT;
- permissões;
- services;
- repositories;
- envio de e-mail;
- Celery;
- exceptions;
- middlewares.

---

## Estrutura de pastas

```text
book-review-api/
├── migrations/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py
│   │   ├── book_controller.py
│   │   ├── review_controller.py
│   │   └── tag_controller.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   ├── book_model.py
│   │   ├── review_model.py
│   │   ├── tag_model.py
│   │   └── book_tag_model.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth_view.py
│   │   ├── user_view.py
│   │   ├── book_view.py
│   │   ├── review_view.py
│   │   └── tag_view.py
│   │
│   └── core/
│       ├── __init__.py
│       ├── config.py
│       ├── database.py
│       ├── redis.py
│       ├── dependencies.py
│       ├── exceptions.py
│       ├── exception_handlers.py
│       ├── middleware.py
│       │
│       ├── security/
│       │   ├── __init__.py
│       │   ├── jwt.py
│       │   ├── password.py
│       │   └── permissions.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── auth_service.py
│       │   ├── book_service.py
│       │   ├── review_service.py
│       │   ├── tag_service.py
│       │   └── user_service.py
│       │
│       ├── repositories/
│       │   ├── __init__.py
│       │   ├── user_repository.py
│       │   ├── book_repository.py
│       │   ├── review_repository.py
│       │   └── tag_repository.py
│       │
│       ├── mail/
│       │   ├── __init__.py
│       │   ├── mail_config.py
│       │   └── mail_service.py
│       │
│       └── tasks/
│           ├── __init__.py
│           ├── celery_app.py
│           └── email_tasks.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_books.py
│   ├── test_health.py
│   ├── test_reviews.py
│   └── test_tags.py
│
├── .env
├── .gitignore
├── alembic.ini
├── compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

## Pré-requisitos

Para rodar a API na sua máquina usando banco e Redis no Docker:

- Python 3.13 ou superior;
- Poetry;
- Docker;
- Docker Compose.

Nesse modo, o Docker é usado apenas para subir PostgreSQL e Redis. Por isso, não é necessário rodar `docker build`.

Para rodar a API e o Celery também dentro de containers, use a seção [Como rodar com Docker](#como-rodar-com-docker). Nesse caso, o build da imagem da aplicação é necessário.

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Se precisar gerar um valor para `JWT_SECRET`, use:

```bash
openssl rand -hex 32
```

Para rodar localmente com PostgreSQL e Redis expostos pelo Docker, confira estes valores no `.env`:

```env
DOMAIN=localhost:8000
JWT_SECRET=<uma-string-aleatoria>
JWT_ALGORITHM=HS256
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/bookly
REDIS_URL=redis://localhost:6379/0
MAIL_FROM=bookly@example.com
```

`MAIL_FROM` precisa ter formato de e-mail válido, mesmo em desenvolvimento. Se ficar vazio, a aplicação pode falhar ao iniciar porque o FastAPI-Mail valida essa configuração.

---

## Como rodar localmente

Este é o fluxo recomendado para desenvolvimento: PostgreSQL e Redis no Docker, API rodando localmente com Poetry.

### 1. Entre na pasta do projeto

```bash
cd book-review-api
```

---

### 2. Crie e configure o `.env`

Crie ou edite o arquivo `.env` na raiz do projeto e use as URLs locais:

```env
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/bookly
REDIS_URL=redis://localhost:6379/0
DOMAIN=localhost:8000
JWT_SECRET=<uma-string-aleatoria>
JWT_ALGORITHM=HS256
MAIL_FROM=bookly@example.com
```

---

### 3. Instale as dependências

```bash
poetry install
```

Não rode `poetry lock` normalmente. Use `poetry lock` apenas se você realmente quiser atualizar o arquivo `poetry.lock`.

---

### 4. Suba PostgreSQL e Redis no Docker

```bash
docker compose up -d db redis
```

Esse comando não faz build da aplicação. Ele baixa/sobe apenas as imagens prontas do PostgreSQL e Redis.

Confira os containers:

```bash
docker compose ps
```

O `compose.yml` já cria o banco `bookly` com:

```text
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=bookly
```

---

### 5. Rode as migrations

```bash
poetry run alembic upgrade head
```

Para conferir a migration atual:

```bash
poetry run alembic current
```

Para conferir as tabelas no PostgreSQL:

```bash
docker compose exec db psql -U postgres -d bookly -c "\dt"
```

---

### 6. Suba a API

```bash
poetry run uvicorn src.main:app --reload
```

A API ficará disponível em:

```text
http://localhost:8000
```

Documentação Swagger:

```text
http://localhost:8000/api/v1/docs
```

Documentação ReDoc:

```text
http://localhost:8000/api/v1/redoc
```

OpenAPI JSON:

```text
http://localhost:8000/api/v1/openapi.json
```

---

### 7. Rode o Celery opcionalmente

O Celery é usado para tarefas em background, como envio de e-mail.

```bash
poetry run celery -A src.core.tasks.celery_app.c_app worker --loglevel=info
```

Se você não configurar SMTP real, endpoints que enfileiram e-mail podem criar tarefas, mas o envio real pode falhar no worker.

---

### 8. Pare os serviços de infraestrutura

```bash
docker compose down
```

Para apagar também o volume do banco e começar do zero:

```bash
docker compose down -v
```

---

## Como rodar com Docker

Use este fluxo quando quiser rodar API, Celery, PostgreSQL e Redis dentro do Docker.

### 1. Configure o `.env`

Crie ou edite o arquivo `.env` na raiz do projeto.

Dentro do Docker Compose, o arquivo `compose.yml` sobrescreve `DATABASE_URL` e `REDIS_URL` para usar os hosts internos `db` e `redis`.

---

### 2. Suba os containers com build

```bash
docker compose up --build -d
```

O Docker Compose sobe os serviços:

- `web`: aplicação FastAPI;
- `db`: PostgreSQL;
- `redis`: Redis;
- `celery`: worker Celery.

---

### 3. Rode as migrations dentro do container

```bash
docker compose exec web poetry run alembic upgrade head
```

---

### 4. Veja os logs

```bash
docker compose logs -f web
```

Para ver todos os serviços:

```bash
docker compose logs -f
```

---

### 5. Acesse a API

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/api/v1/docs
```

---

### 6. Parar os containers

```bash
docker compose down
```

Para remover também os volumes:

```bash
docker compose down -v
```

---

## Migrations com Alembic

### Rodar migrations

```bash
poetry run alembic upgrade head
```

Com Docker:

```bash
docker compose exec web poetry run alembic upgrade head
```

---

### Criar uma nova migration

```bash
poetry run alembic revision --autogenerate -m "create table name"
```

---

### Voltar uma migration

```bash
poetry run alembic downgrade -1
```

---

### Ver histórico

```bash
poetry run alembic history
```

---

### Ver migration atual

```bash
poetry run alembic current
```

---

## Celery e tarefas assíncronas

O projeto usa Celery para executar tarefas em background, principalmente envio de e-mails.

Com Docker, o serviço `celery` já sobe junto com o Compose.

Para rodar localmente:

```bash
poetry run celery -A src.core.tasks.celery_app.c_app worker --loglevel=info
```

O Celery usa Redis como broker/backend.

---

## Testes

Rodar todos os testes:

```bash
poetry run pytest
```

Rodar com saída resumida:

```bash
poetry run pytest -q
```

Rodar com saída detalhada:

```bash
poetry run pytest -v
```

Rodar um arquivo específico:

```bash
poetry run pytest tests/test_health.py
```

---

## Documentação da API

Depois de subir o servidor, acesse:

```text
http://localhost:8000/api/v1/docs
```

Esse endereço abre a documentação Swagger gerada automaticamente pelo FastAPI.

Também existe a documentação ReDoc:

```text
http://localhost:8000/api/v1/redoc
```

---

## Fluxo de autenticação

O projeto usa autenticação baseada em JWT.

Fluxo básico:

```text
1. Usuário cria conta em /api/v1/auth/signup
2. API envia e-mail de verificação
3. Usuário verifica a conta pelo link
4. Usuário faz login em /api/v1/auth/login
5. API retorna access_token e refresh_token
6. Usuário envia o access_token no header Authorization
7. Para logout, o token é colocado em blocklist no Redis
```

Formato do header autenticado:

```http
Authorization: Bearer <access_token>
```

---

## Endpoints principais

### Health

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Mensagem inicial da API |
| GET | `/health` | Verifica se a API está ativa |

---

### Auth

Prefixo:

```text
/api/v1/auth
```

| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| POST | `/signup` | Cria uma nova conta | Não |
| GET | `/verify/{token}` | Verifica conta por token enviado por e-mail | Não |
| POST | `/login` | Autentica usuário e retorna tokens JWT | Não |
| GET | `/refresh_token` | Gera novo access token usando refresh token | Refresh token |
| GET | `/me` | Retorna dados do usuário autenticado | Sim |
| GET | `/logout` | Revoga token atual usando Redis blocklist | Sim |
| POST | `/password-reset-request` | Solicita redefinição de senha | Não |
| POST | `/password-reset-confirm/{token}` | Confirma redefinição de senha | Não |
| POST | `/send_mail` | Envia e-mail manualmente | Não |

---

### Books

Prefixo:

```text
/api/v1/books
```

| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| GET | `/` | Lista todos os livros | Sim |
| GET | `/user/{user_uid}` | Lista livros de um usuário | Sim |
| POST | `/` | Cria um novo livro | Sim |
| GET | `/{book_uid}` | Busca livro por UID | Sim |
| PATCH | `/{book_uid}` | Atualiza livro por UID | Sim |
| DELETE | `/{book_uid}` | Remove livro por UID | Sim |

---

### Reviews

Prefixo:

```text
/api/v1/reviews
```

| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| GET | `/` | Lista todas as reviews | Sim, admin |
| GET | `/{review_uid}` | Busca review por UID | Sim |
| POST | `/book/{book_uid}` | Cria review para um livro | Sim |
| DELETE | `/{review_uid}` | Remove review por UID | Sim |

---

### Tags

Prefixo:

```text
/api/v1/tags
```

| Método | Endpoint | Descrição | Auth |
|---|---|---|---|
| GET | `/` | Lista todas as tags | Sim |
| POST | `/` | Cria uma nova tag | Sim |
| POST | `/book/{book_uid}/tags` | Associa tags a um livro | Sim |
| PUT | `/{tag_uid}` | Atualiza tag por UID | Sim |
| DELETE | `/{tag_uid}` | Remove tag por UID | Sim |

---

## Exemplos de payloads

### Criar usuário

```http
POST /api/v1/auth/signup
```

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "testpass123"
}
```

---

### Login

```http
POST /api/v1/auth/login
```

```json
{
  "email": "johndoe@example.com",
  "password": "testpass123"
}
```

Resposta esperada:

```json
{
  "message": "Login successful",
  "access_token": "jwt-access-token",
  "refresh_token": "jwt-refresh-token",
  "user": {
    "email": "johndoe@example.com",
    "uid": "user-uuid"
  }
}
```

---

### Criar livro

```http
POST /api/v1/books
Authorization: Bearer <access_token>
```

```json
{
  "title": "Clean Architecture",
  "author": "Robert C. Martin",
  "publisher": "Pearson",
  "published_date": "2017-09-20",
  "page_count": 432,
  "language": "English"
}
```

---

### Atualizar livro

```http
PATCH /api/v1/books/{book_uid}
Authorization: Bearer <access_token>
```

```json
{
  "title": "Clean Architecture",
  "author": "Robert C. Martin",
  "publisher": "Pearson",
  "page_count": 432,
  "language": "English"
}
```

---

### Criar review para um livro

```http
POST /api/v1/reviews/book/{book_uid}
Authorization: Bearer <access_token>
```

```json
{
  "rating": 4,
  "review_text": "Livro muito bom para entender arquitetura de software."
}
```

> Observação: atualmente o schema usa `rating < 5`, então o valor máximo aceito é `4`.

---

### Criar tag

```http
POST /api/v1/tags
Authorization: Bearer <access_token>
```

```json
{
  "name": "software-architecture"
}
```

---

### Adicionar tags a um livro

```http
POST /api/v1/tags/book/{book_uid}/tags
Authorization: Bearer <access_token>
```

```json
{
  "tags": [
    {
      "name": "backend"
    },
    {
      "name": "architecture"
    }
  ]
}
```

---

## Comandos úteis

### Instalar dependências

```bash
poetry install
```

---

### Adicionar dependência

```bash
poetry add nome-do-pacote
```

---

### Adicionar dependência de desenvolvimento

```bash
poetry add --group dev nome-do-pacote
```

---

### Rodar servidor local

```bash
poetry run uvicorn src.main:app --reload
```

---

### Rodar testes

```bash
poetry run pytest
```

---

### Rodar lint com Ruff

```bash
poetry run ruff check .
```

---

### Rodar formatação com Black

```bash
poetry run black .
```

---

### Ordenar imports com Isort

```bash
poetry run isort .
```

---

### Validar Docker Compose

```bash
docker compose config
```

---

### Subir containers

```bash
docker compose up --build
```

---

### Subir containers em background

```bash
docker compose up --build -d
```

---

### Ver logs

```bash
docker compose logs -f
```

---

### Derrubar containers

```bash
docker compose down
```

---

## Observações importantes

Verifique se a versão do Python no `pyproject.toml` está compatível com a imagem do `Dockerfile`.

Exemplo:

- se o `pyproject.toml` exigir `>=3.13`, a imagem Docker também deve usar Python 3.13;
- se o Dockerfile usar `python:3.12-slim`, o `pyproject.toml` não deve exigir Python 3.13.

Caso contrário, o `poetry install` pode falhar dentro do container.

---

### 3. Migrations não rodam automaticamente

Depois de subir banco e API, rode:

```bash
poetry run alembic upgrade head
```

Ou, com Docker:

```bash
docker compose exec web poetry run alembic upgrade head
```

---

### 4. O e-mail precisa de configuração real

Para envio real de e-mail, configure:

```env
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=bookly@example.com
```

Para Gmail, normalmente é necessário usar senha de app.

---

### 5. Redis é necessário para logout e Celery

O Redis é usado para:

- blocklist de tokens JWT no logout;
- broker/backend do Celery.

Se Redis não estiver rodando, logout e tasks assíncronas podem falhar.

---

## Licença

Este projeto está sob licença MIT.

---

## Autor

Desenvolvido por **dgusfr**.
