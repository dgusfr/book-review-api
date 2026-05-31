# FastAPI User Management API

API RESTful desenvolvida com FastAPI seguindo **Clean Architecture**, com gerenciamento de dependências e ambiente por Poetry.

## Requisitos

- Python 3.13+
- Poetry 2.0+

## 📁 Estrutura do Projeto

```
python_FastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py                          # Entrada da aplicação FastAPI
│   ├── database/
│   │   └── connection.py                # Configuração de banco de dados
│   ├── models/
│   │   └── user.py                      # Definição da tabela User (SQLAlchemy Core)
│   ├── schemas/
│   │   └── user_schema.py               # Validação Pydantic (Request/Response)
│   ├── services/
│   │   └── user_service.py              # Lógica de negócio
│   ├── controllers/
│   │   └── user_controller.py           # Orquestração de requisições
│   ├── routes/
│   │   └── user_routes.py               # Definição das rotas HTTP
│   └── server/
│       └── run_server.py                # Script para iniciar servidor
├── app.db                               # Banco de dados SQLite (gerado)
├── pyproject.toml                       # Dependências do projeto
├── seed.py                              # Script para popular dados iniciais
└── README.md                            # Este arquivo
```

## ⚙️ Configuração

### 1. Instalar dependências

```bash
poetry install
```

### 2. Ativar o ambiente (opcional)

```bash
poetry shell
```

## 🚀 Rodar o Servidor

### Opção 1: Com Poetry (recomendado)

```bash
poetry run uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

### Opção 2: Executar script

```bash
python app/server/run_server.py
```

### Opção 3: Dentro do shell Poetry

```bash
poetry shell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

**Server:** http://127.0.0.1:8001  
**Docs:** http://127.0.0.1:8001/docs

## 📊 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Mensagem de boas-vindas |
| GET | `/health` | Status de saúde |
| GET | `/users` | Listar todos os usuários |
| POST | `/users` | Criar novo usuário |
| GET | `/users/{id}` | Obter usuário por ID |
| PUT | `/users/{id}` | Atualizar usuário |
| DELETE | `/users/{id}` | Deletar usuário |

### Exemplos de Uso

**Listar usuários:**
```bash
curl http://127.0.0.1:8001/users
```

**Criar usuário:**
```bash
curl -X POST http://127.0.0.1:8001/users \
  -H "Content-Type: application/json" \
  -d '{"username":"João","email":"joao@example.com"}'
```

**Obter usuário:**
```bash
curl http://127.0.0.1:8001/users/1
```

**Atualizar usuário:**
```bash
curl -X PUT http://127.0.0.1:8001/users/1 \
  -H "Content-Type: application/json" \
  -d '{"username":"João Silva","email":"joao.silva@example.com"}'
```

**Deletar usuário:**
```bash
curl -X DELETE http://127.0.0.1:8001/users/1
```

## 🌱 Popular Banco de Dados

```bash
poetry run python seed.py
```

Insere 3 usuários iniciais na base.

## 🗄️ Banco de Dados

- **Tipo:** SQLite
- **Arquivo:** `app.db`
- **Acesso:** Async via `databases`

Tabelas criadas automaticamente no startup.

## 🏗️ Arquitetura Clean

- **Routes:** Endpoints HTTP
- **Controllers:** Orquestração
- **Services:** Lógica de negócio
- **Models:** Estrutura das tabelas
- **Schemas:** Validação Pydantic
- **Database:** Conexão e metadata

## 📝 Schema

**Tabela `users`:**

| Campo | Tipo | Restrições |
|-------|------|-----------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| username | STRING(255) | NOT NULL, INDEXED |
| email | STRING(255) | NULLABLE |

## 📦 Dependências Principais

- FastAPI
- Uvicorn
- SQLAlchemy
- databases
- Pydantic

Ver `pyproject.toml` para lista completa.