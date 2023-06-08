from time import sleep
from os import system

def setup_admin_user():
    username = input('Digite um nome de usuário: ')
    while True:
        password = input('Digite uma senha: ')
        confirm_password = input('Confirme sua senha: ')
        if password == confirm_password:
            break
        else:
            system('cls')
            print('As senhas não são iguais.')
    return (username, password, 'admin')

def setup_hotel():
    pass

def print_sleep_clean(message, time):
    print(message)
    sleep(time)
    system('cls')

def greetings():
    print_sleep_clean('Olá, usuário!', 5)
    print_sleep_clean('Vejo que é a sua primeira vez acessando nossa aplicação, bem-vindo!', 5)
    print_sleep_clean('Permita-me ajudar com a configuração do sistema...', 5)
    print_sleep_clean('Primeiro, vamos criar uma conta', 5)
