from time import sleep
from os import system

def setup_user(function_user, hotel_id):
    return function_user(hotel_id)

def setup_hotel(function_hotel):
    return function_hotel()

def print_sleep_clean(message, time):
    print(message)
    sleep(time)
    system('cls')

def greetings():
    system('cls')
    print_sleep_clean('Olá, usuário!', 2)
    print_sleep_clean('Vejo que é a sua primeira vez acessando nossa aplicação, bem-vindo!', 5)
    print_sleep_clean('Permita-me ajudar com a configuração do sistema...', 4)
    print_sleep_clean('Primeiro, vamos criar uma conta', 3)

def continue_setup():
    system('cls')
    print_sleep_clean('Conta criada, agora vamos cadastrar o Hotel', 4)

def finish_setup():
    system('cls')
    print_sleep_clean('Tudo pronto! Agora você já pode usar o sistema!', 4)
