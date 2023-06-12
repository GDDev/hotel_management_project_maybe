from globals import db_name
from os import system
from data.user_database import UserDatabase 
from utils.custom_exceptions import LoginError

DB = UserDatabase(db_name)

# Criando uma classe pai para os tipos de funcionário
class User:
    # Definindo os atributos comuns
    def __init__(self, id, name, last_name, email, username, password, hotel_id, role):
        self.user_id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.role = role
        self.hotel = hotel_id

    def create_user(hotel_id):
        full_name = input('Informe o nome completo do funcionário: ')
        name = full_name[0]
        last_name = full_name[1:len(full_name)]
        last_name = ' '.join(last_name)
        email = input('Informe o e-mail do funcionário: ')
        username = input('Digite um nome de usuário: ')
        while True:
            password = input('Digite uma senha: ')
            confirm_password = input('Confirme sua senha: ')
            if password == confirm_password:
                break
            else:
                system('cls')
                print('As senhas não são iguais.')
        role = input('Informe o tipo de usuário (padrão para recepcionista): ')
        role = 'admin' if role.lower() == 'admin' else 'receptionist'

        user = (name, last_name, email, username, password, role, hotel_id)
        user_id = DB.insert_user(user)
        if role == 'admin':
            user = Admin(user_id, name, last_name, email, username, password, role, hotel_id)
        else:
            user = Receptionist(user_id, name, last_name, email, username, password, role, hotel_id)
        return user

    def get_all_users(hotel_id):
        user_list = []
        users = DB.get_hotel_staff(hotel_id)
        for user in users:
            user_id, name, last_name, email, username, password, role, hotel = user
            if role == 'admin':
                user_class = Admin(user_id, name, last_name, email, username, password, role, hotel)
            else:
                user_class = Receptionist(user_id, name, last_name, email, username, password, role, hotel)
            user_list.append(user_class)
        return user_list
    
    # Definindo a função de validação de login
    def perform_login(self, hotel_id):
        # Buscando os usuários registrados no banco de dados
        users = self.get_all_users(hotel_id)

        # Lendo as credenciais do usuário
        username = input('Usuário: ')
        password = input('Senha: ')

        # Definindo quantidade máxima de tentativas de login, antes de encerrar o programa
        attempts = 3
        while attempts > 1:
            # Iterando sobre os usuários encontrados
            for user in users:
                # Verificando a compatibilidade entre os nomes de usuário
                if user.username == username:
                    # Chamando função para comparar a senha fornecida com a armazenada
                    if UserDatabase.compare_password(password, user.password):
                        # Retornando o usuário logado
                        system('cls')
                        return user
            # Limpando o console
            system('cls')
            # Diminuindo uma tentativa restante
            attempts -= 1
            print(f'Credenciais erradas, tente novamente. Tentativas restantes {attempts}')
        raise LoginError()

# Criando uma classe específica para funcionários com maior permissionamento
class Admin(User):
    # Criando usuário admin
    def __init__(self, user_id, name, last_name, email, username, password, role, hotel_id):
        super().__init__(user_id, name, last_name, email, username, password, role, hotel_id)

class Receptionist(User):
    # Criando funcionário comum
    def __init__(self, user_id, name, last_name, email, username, password, role, hotel_id):
        super().__init__(user_id, name, last_name, email, username, password, role, hotel_id)
