# FastAPI API

API simples criada com FastAPI.

## Requisitos

- Python 3.10+
- pip

## Ambiente virtual

### Windows (PowerShell)

```bash
python -m venv .venv
.\venv\Scripts\Activate.ps1
```

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalacao de dependencias

```bash
pip install "fastapi[standard]"
```

## Rodar o servidor

```bash
fastapi dev
```

## Notas

- Se o comando `fastapi dev` nao for encontrado, verifique se o ambiente virtual esta ativado.