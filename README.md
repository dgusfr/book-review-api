# FastAPI API

API simples criada com FastAPI, com dependencias e ambiente gerenciados 100% pelo Poetry.

## Requisitos

- Python 3.10+
- Poetry

## Instalar o Poetry

Recomendado via pipx:

```bash
pipx install poetry
```

Se nao tiver o pipx instalado:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

## Configurar o ambiente com Poetry

### 1) (Opcional) Manter o ambiente virtual dentro do projeto

```bash
poetry config virtualenvs.in-project true
```

### 2) Inicializar o projeto (se ainda nao existir `pyproject.toml`)

```bash
poetry init
```

Quando for perguntado pelas dependencias, adicione:

```bash
fastapi[standard]
```

### 3) Instalar dependencias

```bash
poetry install
```

## Rodar o servidor

```bash
poetry run fastapi dev main.py
```

Ou entrar no shell do Poetry e rodar o comando direto:

```bash
poetry shell
fastapi dev main.py
```