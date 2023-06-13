from classes.guest import Guest
# from classes.hotel import Hotel
from data.user_database import UserDatabase 
from globals import db_name
from os import system
from utils.custom_exceptions import InvalidChoiceError, InvalidInputError, LoginError
from utils.farewell import random_farewell
from utils.menus import menu, staff_management_menu, user_management_menu
# from utils.menus import 
from utils.validate_input import validate_email, validate_name, validate_username

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
        while True:
            try:
                full_name = input('Informe o nome completo do funcionário: ')
                name, last_name = validate_name(full_name)
                email = input('Informe o e-mail do funcionário: ')
                validate_email(email)
                username = input('Digite um nome de usuário: ')
                validate_username(username)
                while True:
                    password = input('Digite uma senha: ')
                    confirm_password = input('Confirme sua senha: ')
                    if password == confirm_password:
                        break
                    else:
                        system('cls')
                        print('As senhas não são iguais.')
                role = input('Informe o tipo de usuário (ENTER para recepcionista): ')
                role = 'admin' if role.lower() == 'admin' else 'receptionist'
                user = (name.upper(), last_name.upper(), email, username, password, role, hotel_id)
                user_id = DB.insert_user(user)
                if role == 'admin':
                    user = Admin(user_id, name.capitalize(), last_name.title(), email, username, password, role, hotel_id)
                else:
                    user = Receptionist(user_id, name.capitalize(), last_name.title(), email, username, password, role, hotel_id)
                print('Funcionário cadastrado com sucesso!')
                input('Pressione ENTER para continuar...')
                return user
            except InvalidInputError as e:
                print(e)
                input('Pressione ENTER para voltar...')
                system('cls')
    
    # Definindo a função de validação de login
    def perform_login(self):
        try:
            # Buscando os usuários registrados no banco de dados
            users = self.get_all_users()

            # Definindo quantidade máxima de tentativas de login, antes de encerrar o programa
            attempts = 3
            while attempts > 0:
                # Lendo as credenciais do usuário
                username = input('Usuário: ')
                validate_username(username)
                password = input('Senha: ')
            
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
        except LoginError as e:
            print(e)
            input('\n Pressione ENTER para continuar...')
        except InvalidInputError as e:
            print(e)
            input('\n Pressione ENTER para continuar...')

    # Função criada para retornar uma lista com todos os usuários
    def get_all_users():
        user_list = []
        # Recebendo uma lista de usuários do banco de dados
        users = DB.get_hotel_staff()
        # Percorrendo a lista
        for user in users:
            # Desempacotando os atributos do usuário
            user_id, name, last_name, email, username, password, role, hotel = user
            # Criando uma instância de Admin se o usuário for admin
            if role == 'admin':
                user_class = Admin(user_id, name, last_name, email, username, password, role, hotel)
            # Criando uma instância de Receptionist se o usuário for receptionist
            else:
                user_class = Receptionist(user_id, name, last_name, email, username, password, role, hotel)
            user_list.append(user_class)
        # Retornando uma lista com as instâncias criadas
        return user_list
    
    def get_user_by_id(user_id):
        user = DB.get_user_by_id(user_id)
        id, name, last_name, email, username, password, role, hotel = user
        if role == 'admin':
            user = Admin(id, name, last_name, email, username, password, role, hotel)
        else:
            user = Receptionist(id, name, last_name, email, username, password, role, hotel)
        return user
    
    def edit_user_info(self):
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
            DB.update_user(self)
        else:
            print('Opção inválida')
        system('cls')

    def change_password(self):
        new_password = input('Nova senha: ')
        if UserDatabase.compare_password(new_password, self.password):
            print('A nova senha não pode ser sua senha atual!')
            return
        else:
            self.password = DB.change_password(self.user_id, new_password)

    def show_user_details(current_hotel):
        current_hotel.refresh_hotel()
        user_list = current_hotel.staff
        for user in user_list:
            print(f'{user.user_id}. {user.name} {user.last_name} ({user.username})')
        choice = input('Informe o ID do funcionário desejado: ')
        int_choice = int(choice)
        user = User.get_user_by_id(int_choice)
        if user:
            system('cls')
            print(f'Nome: {user.name} {user.last_name}\nE-mail: {user.email}')
            print(f'Username: {user.username}\nHotel: {current_hotel.name}')
            choice = menu(user_management_menu, current_hotel, user, User.edit_user_info, User.change_password)
            if choice == '1':
                user.edit_user_info()
            elif choice == '2':
                user.change_password()
            elif choice == '3':
                pass
            input('\nPressione Enter para voltar...')

    def show_all_staff():
        user_list = User.get_all_users()
        for user in user_list:
            print(f'{user.user_id}. {user.name} {user.last_name} ({user.username})')
        input('\nPressione Enter para voltar...')
        system('cls')

    def eliminate_user(current_hotel):
        users = User.get_all_users()
        if len(users) > 1:
            current_hotel.refresh_hotel()
            user_list = current_hotel.staff
            for user in user_list:
                print(f'{user.user_id}. {user.name} {user.last_name} ({user.username})')
            choice = input('Informe o ID do funcionário a ser deletado: ')
            int_choice = int(choice)
            user = User.get_user_by_id(int_choice)
            DB.delete_user(user.user_id)
            current_hotel.refresh_hotel()
        else:
            print('Você não pode excluir o único funcionário cadastrado!')
        input('\nPressione Enter para voltar...')
        system('cls')

    # Função para gerenciamento de funcionários
    def staff_management(current_hotel):
        while True:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            result = menu(staff_management_menu, current_hotel, User.create_user, User.show_user_details, User.show_all_staff, User.eliminate_user)
            if result:
                print(result)
                print('\nPressione ENTER para voltar...')
                break   

# Criando uma classe específica para funcionários com maior permissionamento
class Admin(User):
    # Criando usuário admin
    def __init__(self, user_id, name, last_name, email, username, password, role, hotel_id):
        super().__init__(user_id, name, last_name, email, username, password, role, hotel_id)    

class Receptionist(User):
    # Criando funcionário comum
    def __init__(self, user_id, name, last_name, email, username, password, role, hotel_id):
        super().__init__(user_id, name, last_name, email, username, password, role, hotel_id)
