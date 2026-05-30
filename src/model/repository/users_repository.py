from model.entities.users import (
    Users,
)
from model.settings.db_connection_handler import (
    db_connection_handler,
)


class UsersRepository:  # Declara a classe responsável por acessar os dados de usuários no banco
    def __init__(self):  # Método executado quando a classe é criada
        self.__connection = (
            db_connection_handler.get_database()
        )  # Guarda a conexão com o banco em um atributo privado

    async def get_all_users(
        self,
    ) -> list:  # Define um método assíncrono que busca todos os usuários e retorna uma lista
        query = Users.select()  # Monta a consulta SQL equivalente a SELECT * FROM users
        rows = await self.__connection.fetch_all(
            query
        )  # Executa a consulta de forma assíncrona e recebe todas as linhas

        users: list = []  # Cria uma lista vazia onde os usuários convertidos serão armazenados
        for row in rows:  # Percorre cada linha retornada pelo banco
            mapping = getattr(
                row, "_mapping", row
            )  # Tenta pegar a versão da linha como dicionário; se não existir, usa a linha direto
            users.append(dict(mapping))  # Converte a linha em dict e adiciona na lista final

        return users  # Retorna a lista de usuários em formato simples
