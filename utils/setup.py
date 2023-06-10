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
    system('cls')
    return (username, password, 'admin')

def setup_hotel(db, function_hotel):
    return function_hotel(db)

def print_sleep_clean(message, time):
    print(message)
    sleep(time)
    system('cls')

def greetings():
    system('cls')
    print_sleep_clean('Olá, usuário!', 5)
    print_sleep_clean('Vejo que é a sua primeira vez acessando nossa aplicação, bem-vindo!', 5)
    print_sleep_clean('Permita-me ajudar com a configuração do sistema...', 5)
    print_sleep_clean('Primeiro, vamos criar uma conta', 5)

def continue_setup():
    print_sleep_clean('Conta criada, agora vamos cadastrar o Hotel', 5)

def finish_setup():
    system('cls')
    print_sleep_clean('Tudo pronto! Agora você já pode usar o sistema!', 5)
