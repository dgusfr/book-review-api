# ERP API

API desenvolvida com FastAPI, com dependências e ambiente gerenciados 100% pelo Poetry.

## Requisitos

- Python 3.13+ (ou versão definida em `pyproject.toml`)
- pyenv (para gerenciar versões do Python)
- Poetry 2.0+

## ⚙️ Configurar o projeto localmente

### 1) Instalar Poetry via pipx (se não tiver)

```bash
python -m pip install --user pipx
python -m pipx ensurepath
pipx install poetry
```

### 2) Clonar o repositório e acessar a pasta

```bash
git clone <seu-repositorio>
cd python_FastAPI
```

### 3) Instalar as dependências do projeto

```bash
poetry install
```

Poetry vai automaticamente:
- Criar um ambiente virtual isolado
- Instalar todas as dependências do `pyproject.toml`
- Usar a versão do Python definida (via `poetry.lock`)

### 4) Verificar a instalação

```bash
poetry run python --version
poetry run python main.py
```

## 🚀 Rodar o servidor

### Opção 1: Rodar comandos com Poetry (recomendado)

```bash
# Servidor de desenvolvimento com hot-reload
poetry run fastapi dev main.py

# Ou rodando como script
poetry run python main.py
```

### Opção 2: Ativar o ambiente virtual

Com Poetry 2.0+:

```bash
poetry env activate
# Agora pode rodar comandos direto
python main.py
```

Se preferir o comando antigo `poetry shell`, instale o plugin:

```bash
poetry self add poetry-plugin-shell
poetry shell
```

## 📦 Gerenciar dependências

### Adicionar uma dependência

```bash
poetry add fastapi
poetry add pytest --group dev
```

### Atualizar dependências

```bash
poetry update
```

### Remover uma dependência

```bash
poetry remove fastapi
```

## 📝 Arquivo de lock

- `pyproject.toml` - Define as dependências do projeto
- `poetry.lock` - Garante versões exatas (sempre fazer commit no GitHub)