import os
from utils.custom_exceptions import LoginError
from data.database import Database

# Definindo a função de validação de login
def perform_login(database, username, password):
    # Buscando os usuários registrados no banco de dados
    users = Database.get_all_users(database)

    # Definindo quantidade máxima de tentativas de login, antes de encerrar o programa
    attempts = 3
    while attempts > 1:
        # Iterando sobre os usuários encontrados
        for user in users:
            user_id, db_user, db_pass, db_role = user
            # Verificando a compatibilidade entre os nomes de usuário
            if db_user == username:
                # Chamando função para comparar a senha fornecida com a armazenada
                if Database.compare_password(password, db_pass):
                    # Retornando o usuário logado
                    return user
        # Limpando o console
        os.system('cls')
        # Diminuindo uma tentativa restante
        attempts -= 1
        print(f'Credenciais erradas, tente novamente. Tentativas restantes {attempts}')
        # Re-lendo as credenciais
        username = input('Usuário: ')
        password = input('Senha: ')
    raise LoginError()
