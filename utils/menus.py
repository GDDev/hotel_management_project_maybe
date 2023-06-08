from utils import custom_exceptions as exp
import os

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
    admin_items = ['5. Gerenciar Hotel', '6. Gerenciar funcionários', '7. Sair']
    menu.extend(admin_items)
    return menu

# Criando menu para gerenciamento de funcionários
def employees_management_menu():
    menu = ['Gerenciamento de Funionários', '1. Adicionar funcionário', '2. Ver detalhes de um funcionáio', '3. Ver todos os funcionários', '4. Deletar um funcionário', '5. Voltar']
    return menu

# Criando função para exibir o menu escolhido
def menu(menu_list):
    # Validando a opção escolhida
    def validate_menu_choice(length):
        while True:
            # Recebendo opção escolhida
            choice = input('Selecione uma opção: ')
            os.system('cls')
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
