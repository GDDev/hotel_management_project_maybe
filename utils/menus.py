from utils import custom_exceptions as exp
from os import system

# Criando o menu de check-in
def checkin_menu():
    # Definindo as opções do menu principal
    menu = ['Check-in', 
            '1. Mostrar quartos disponíveis', 
            '2. Hospedar', 
            '3. Voltar']
    return menu

# Criando o menu de check-out
def checkout_menu():
    # Definindo as opções do menu principal
    menu = ['Check-out', 
            '1. Localizar hospedagem', 
            '2. Voltar']
    return menu

# Criando menu para gerenciamento do hotel
def hotel_management_menu():
    system('cls')
    # Definindo opções
    menu = ['Gerenciamento do Hotel',
            '1. Visualizar todos os hotéis',
            '2. Cadastrar novo hotel',
            '3. Atualizar hotel',
            '4. Excluir hotel',
            '5. Voltar']
    return menu  

# Criando menu para gerenciamento de funcionários
def staff_management_menu():
    menu = ['Gerenciamento de Funionários', 
            '1. Adicionar funcionário', 
            '2. Ver detalhes de um funcionáio', 
            '3. Ver todos os funcionários', 
            '4. Deletar um funcionário', 
            '5. Voltar']
    return menu

# Criando o menu principal
def main_menu():
    # Definindo as opções do menu principal
    menu = ['Menu', 
            '1. Check-in', 
            '2. Check-out', 
            '3. Mostrar quartos disponíveis',
            '4. Localizar hóspede', 
            '5. Sair']
    return menu

# Criando menu para ADMINs
def admin_menu():
    # Definindo opções
    menu = main_menu()
    menu.pop()
    admin_items = ['5. Gerenciar Hotel', 
                    '6. Gerenciar funcionários', 
                    '7. Sair']
    menu.extend(admin_items)
    return menu

def update_hotel_menu():
    menu = ['Atualizar Hotel', 
            '1. Adicionar quarto', 
            '2. Adicionar funcionário', 
            '3. Editar Hotel', 
            '4. Voltar']
    return menu

# Criando função para exibir o menu escolhido
def menu(menu_list):
    # Validando a opção escolhida
    def validate_menu_choice(length):
        while True:
            # Recebendo opção escolhida
            choice = input('Selecione uma opção: ')
            system('cls')
            # Verificando se é uma das existentes
            if int(choice) in range(1, length):
                # Opção válida é retornada
                return choice
            raise exp.InvalidChoiceError()
    # Atribuindo a lista recebida à uma variável
    show_menu = menu_list()
    # Exibindo o menu
    for line in show_menu:
        print(line)
    # Recebendo número de opções do menu (não precisa descontar por causa do título)
    length = len(show_menu)
    # Vendo se o usuário digitou uma opção válida
    choice = validate_menu_choice(length)
    # Retornando a escolha do usuário
    return choice
