# API de Gerenciamento Escolar - FastAPI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

Esta aplicação foi desenvolvida para gerenciar o ecossistema de uma instituição de ensino, controlando desde o cadastro básico de alunos e professores até a gestão de perfis detalhados e matrículas em disciplinas. O foco principal é demonstrar o uso de relações complexas em bancos de dados relacionais integrados ao FastAPI.


---

## Tabela de Conteúdos

* [Arquitetura](#arquitetura)
* [Tech Stack](#tech-stack)
* [Documentação da API](#documentação-da-api)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Melhorias Futuras](#melhorias-futuras)

---

---

## Arquitetura

O projeto utiliza o **SQLAlchemy** como ORM para mapear o banco de dados PostgreSQL, garantindo a integridade referencial entre as tabelas.

### Destaques Técnicos:

* **Relação 1:1 (One-to-One)**: Implementação entre `Estudante` e `Perfil`, onde cada aluno possui um registro único de detalhes adicionais como idade e endereço.
* **Relação 1:N (One-to-Many)**: Vínculo entre `Professor` e seus `Estudantes` associados através da chave estrangeira `professor_id`.
* **Relação N:N (Many-to-Many)**: Gerenciada pela tabela de associação `Matricula`, conectando os IDs de `Estudante` e `Disciplina`.
* **Carregamento Otimizado**: Uso de `joinedload` para carregar o perfil do estudante em uma única consulta ao banco, evitando múltiplas requisições (N+1 problem).

---

---

## Documentação da API

### Estudantes e Perfis

Criação de estudante com criação automática de perfil vinculado.
**Endpoint**: `POST /estudantes/`

```bash
curl -X POST http://localhost:8000/estudantes/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Gustavo Rocha",
    "email": "gustavo.rocha@didatica.com",
    "perfil": {
        "idade": 16,
        "endereco": "Rua das Flores, 123"
    }
}'

```

---

### Disciplinas

Gerenciamento das matérias oferecidas na instituição.
**Endpoint**: `GET /disciplinas/`

```bash
curl -X GET http://localhost:8000/disciplinas/

```

---

### Professores

Cadastro de docentes responsáveis pelos alunos.
**Endpoint**: `POST /professores/`

```bash
curl -X POST http://localhost:8000/professores/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Fábio Santos"
}'

```

---

### Matrículas

Vinculação de alunos às disciplinas existentes através de seus IDs.
**Endpoint**: `POST /matriculas/`

```bash
curl -X POST http://localhost:8000/matriculas/ \
-H "Content-Type: application/json" \
-d '{
    "estudante_id": 1,
    "disciplina_id": 7
}'

```

---

Desenvolvido por **Diego Franco**
