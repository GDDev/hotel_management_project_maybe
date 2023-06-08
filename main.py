# Importando tudo o que vai usar
import os
from classes import hotel as ht, guest as gt, room as rm, user as usr
from utils import menus as mn, farewell as fw, login as lg, custom_exceptions as exp
from data import database

# Definindo uma função para logar o usuário
def login():
    # Lendo as credenciais do usuário
    username = input('Usuário: ')
    password = input('Senha: ')

    # Chamando a função de validação do login
    user = lg.perform_login(db, username, password)
    user_role = user[3]
        
    # Definindo o tipo de usuário logado
    if user_role == 'admin':
        return usr.Admin(username, password)
    elif user_role == 'employee':
        return usr.Employee(username, password)

# Função para gerenciamento de funcionários
def employee_management():
    while True:
        mn.employees_management_menu()
        choice = mn.validate_emp_mng_menu_choice()
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            return

# Definindo o escopo principal
def main():

    while True:
        # Exibindo o menu principal
        if user.role == 'admin':
            mn.admin_main_menu()
            try:
                # Lendo a escolha do usuário
                choice = mn.validate_admin_main_menu_choice()

                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    employee_management()
                elif choice == '6':
                    # Encerrando o programa
                    print(fw.random_farewell())
                    break
            except exp.InvalidChoiceError as e:
                print(e)
        else:
            mn.main_menu()
            try:
                # Lendo a escolha do usuário
                choice = mn.validate_main_menu_choice()

                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    # Encerrando o programa
                    print(fw.random_farewell())
                    break
            except exp.InvalidChoiceError as e:
                print(e)

# Iniciando o programa
if __name__ == '__main__':
    try:
        # Conectando com o banco de dados
        db = database.Database('hotel.db')
        # Executando a função de inicialização do bd
        db.initialize()
        # Executando o login
        user = login()
        # Executando o programa
        main()
    except exp.LoginError as e:
        os.system('cls')
        print(e)
