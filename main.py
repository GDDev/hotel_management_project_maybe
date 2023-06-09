# Importando tudo o que vai usar
import os
from classes.hotel import Hotel
# from classes.guest import Guest 
# from classes.room import Room
from classes.admin import Admin
from classes.receptionist import Receptionist 
from utils import menus
from utils.farewell import random_farewell 
from utils.login import perform_login 
from utils import custom_exceptions
from data import database

# Definindo uma função para logar o usuário
def login():
    # Lendo as credenciais do usuário
    username = input('Usuário: ')
    password = input('Senha: ')

    # Chamando a função de validação do login
    *_, db_role = perform_login(db, username, password)
        
    # Definindo o tipo de usuário logado
    os.system('cls')
    if db_role == 'admin':
        return Admin(username, password)
    elif db_role == 'receptionist':
        return Receptionist(username, password)
    
def check_in():
    while True:
        # Chamando o menu e recebendo a opção escolhida
        choice = menus.menu(menus.checkin_menu)
        if choice == '1':
            logged_user.display_available_rooms()
            input('Pressione Enter para voltar...')
        elif choice == '2':
            logged_user.checkin_guest()
            input('Pressione Enter para voltar...')
        elif choice == '3':
            break

def check_out():
    while True:
        # Chamando o menu e recebendo a opção escolhida
        choice = menus.menu(menus.checkout_menu)
        if choice == '1':
            logged_user.display_occupied_room_info()
            input('Pressione Enter para voltar...')
        elif choice == '2':
            break

def hotel_management():
    while True:
        # Chamando o menu e recebendo a opção escolhida
        choice = menus.menu(menus.hotel_management_menu)
        if choice == '1':
            Hotel.display_hotels(db)
            input('Pressione Enter para voltar...')
        elif choice == '2':
            Hotel.create_new_hotel(db)
            input('Pressione Enter para voltar...')
        elif choice == '3':
            Hotel.update_hotel_info(db)
            input('Pressione Enter para voltar...')
        elif choice == '4':
            Hotel.delete_hotel(db)
            input('Pressione Enter para voltar...')
        elif choice == '5':
            break

# Função para gerenciamento de funcionários
def staff_management():
    while True:
        # Chamando o menu e recebendo a opção escolhida
        choice = menus.menu(menus.staff_management_menu)
        if choice == '1':
            logged_user.add_employee()
        elif choice == '2':
            logged_user.show_employee_info()
        elif choice == '3':
            logged_user.show_staff()
        elif choice == '4':
            logged_user.delete_employee()
        elif choice == '5':
            break

# Definindo o escopo principal
def main():

    while True:
        # Exibindo o menu principal
        if isinstance(logged_user, Admin):
            try:
                # Chamando o menu e recebendo a opção escolhida
                choice = menus.menu(menus.admin_menu)

                if choice == '1':
                    check_in()
                elif choice == '2':
                    check_out()
                elif choice == '3':
                    logged_user.display_available_rooms()
                elif choice == '4':
                    logged_user.display_occupied_room_info()
                elif choice == '5':
                    hotel_management()
                elif choice == '6':
                    staff_management()
                elif choice == '7':
                    # Encerrando o programa
                    print(random_farewell())
                    break
            except custom_exceptions.InvalidChoiceError as e:
                print(e)
        else:
            try:
                # Chamando o menu e recebendo a opção escolhida
                choice = menus.menu(menus.main_menu)

                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    # Encerrando o programa
                    print(random_farewell())
                    break
            except custom_exceptions.InvalidChoiceError as e:
                print(e)

# Conectando com o banco de dados
db = database.Database('hotel.db')
# Iniciando o programa
if __name__ == '__main__':
    try:
        if not os.path.isfile('hotel.db'):
            # Executando a função de inicialização do bd
            username, password = db.initialize()
            logged_user = Admin(username, password)
        else:
            # Executando o login
            logged_user = login()
        # Executando o programa
        main()
    except custom_exceptions.LoginError as e:
        os.system('cls')
        print(e)
