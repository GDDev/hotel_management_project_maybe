from globals import db_name
from os import system
from data.user_database import UserDatabase 
from utils.custom_exceptions import LoginError

DB = UserDatabase(db_name)

# Criando uma classe pai para os tipos de funcionário
class User:
    # Definindo os atributos comuns
    def __init__(self, id, name, last_name, email, username, password, role, hotel_id):
        self.user_id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.role = role
        self.hotel = hotel_id

    def create_user(hotel_id):
        full_name = input('Informe o nome completo do funcionário: ').split(' ')
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
    
    def get_user_by_id(user_id, hotel_id):
        user = DB.get_user_by_id(user_id, hotel_id)
        id, name, last_name, email, username, password, role, hotel = user
        if role == 'admin':
            user = Admin(id, name, last_name, email, username, password, role, hotel)
        else:
            user = Receptionist(id, name, last_name, email, username, password, role, hotel)
        return user
    
    def edit_user_info(self, hotel_id):
        def change_user_name():
            name = input('Informe o novo nome do Funcionário: ')
            return name
        def change_user_last_name():
            last_name = input('Informe o novo sobrenome do Funcionário: ')
            return last_name
        def change_user_email():
            email = input('Informe o novo e-mail do Funcionário: ')
            return email
        def change_user_username():
            username = input('Informe o novo nome de usuário do Funcionário: ')
            return username
        
        menu = ['Alterar informação',
                f'1. Nome = {self.name}',
                f'2. Sobrenome = {self.last_name}',
                f'3. E-mail = {self.email}',
                f'4. Nome de usuário = {self.username}']
        system('cls')
        # Exibindo o menu
        for line in menu:
            print(line)
        # Recebendo número de opções do menu (não precisa descontar por causa do título)
        length = len(menu)
        choice = input('Selecione uma opção: ')
        # Vendo se o usuário digitou uma opção válida
        if int(choice) in range(1, length):
            system('cls')
            if choice == '1':
                self.name = change_user_name()
            elif choice == '2':
                self.last_name = change_user_last_name()
            elif choice == '3':
                self.email = change_user_email()
            elif choice == '4':
                self.username = change_user_username()
            DB.update_user(self, hotel_id)
        else:
            print('Opção inválida')

    def change_password(self):
        new_password = input('Nova senha: ')
        if UserDatabase.compare_password(new_password, self.password):
            print('A nova senha não pode ser sua senha atual!')
            return
        else:
            self.password = DB.change_password(self.user_id, new_password)

    def delete_user(self, hotel):
        DB.delete_user(self.user_id)
        hotel.remove_employee(self)
    
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
