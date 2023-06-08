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
    os.system('cls')
    if user_role == 'admin':
        return usr.Admin(username, password)
    elif user_role == 'employee':
        return usr.Employee(username, password)

# Função para gerenciamento de funcionários
def employee_management():
    while True:
        # Chamando o menu e recebendo a opção escolhida
        choice = mn.menu(mn.employees_management_menu)
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
            try:
                # Chamando o menu e recebendo a opção escolhida
                choice = mn.menu(mn.admin_menu)

                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    pass
                elif choice == '6':
                    employee_management()
                elif choice == '7':
                    # Encerrando o programa
                    print(fw.random_farewell())
                    break
            except exp.InvalidChoiceError as e:
                print(e)
        else:
            try:
                # Chamando o menu e recebendo a opção escolhida
                choice = mn.menu(main_menu)

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
                    print(fw.random_farewell())
                    break
            except exp.InvalidChoiceError as e:
                print(e)

# Iniciando o programa
if __name__ == '__main__':
    try:
        if not os.path.isfile('hotel.db'):
            # Conectando com o banco de dados
            db = database.Database('hotel.db')
            # Executando a função de inicialização do bd
            db.initialize()
        else:
            # Conectando com o banco de dados
            db = database.Database('hotel.db')
            # Executando o login
            user = login()
        # Executando o programa
        main()
    except exp.LoginError as e:
        os.system('cls')
        print(e)
