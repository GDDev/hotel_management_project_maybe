from utils import custom_exceptions as exp
import os

# Criando o menu principal
def main_menu():
    # Mostrando as opções do menu principal
    print('Menu\n'
          '1. Check-in\n'
          '2. Check-out\n'
          '3. Mostrar quartos disponíveis\n'
          '4. Sair')
# Validando a opção escolhida
def validate_main_menu_choice():
    while True:
        # Recebendo opção escolhida
        choice = input('Selecione uma opção: ')
        os.system('cls')
        # Verificando se é uma das existentes
        if choice in ['1', '2', '3', '4']:
            # Opção válida é retornada
            return choice
        raise exp.InvalidChoiceError()

# Criando menu para ADMINs
def admin_main_menu():
    # Mostrandos opções
    print('Menu\n'
          '1. Check-in\n'
          '2. Check-out\n'
          '3. Mostrar quartos disponíveis\n'
          '4. Gerenciar Hotel\n'
          '5. Gerenciar funcionários\n'
          '6. Sair')
# Validando a opção escolhida
def validate_admin_main_menu_choice():
    while True:
        # Recebendo opção escolhida
        choice = input('Selecione uma opção: ')
        os.system('cls')
        # Verificando se é uma das existentes
        if choice in ['1', '2', '3', '4', '5', '6']:
            # Opção válida é retornada
            return choice
        raise exp.InvalidChoiceError()

# Criando menu para gerenciamento de funcionários
def employees_management_menu():
    print('Gerenciamento de Funionários\n'
          '1. Adicionar funcionário\n'
          '2. Ver detalhes de um funcionáio\n'
          '3. Ver todos os funcionários\n'
          '4. Deletar um funcionário\n'
          '5. Voltar')
# Validando a opção escolhida
def validate_emp_mng_menu_choice():
    while True:
        # Recebendo opção escolhida
        choice = input('Selecione uma opção: ')
        os.system('cls')
        # Verificando se é uma das existentes
        if choice in ['1', '2', '3', '4', '5']:
            # Opção válida é retornada
            return choice
        raise exp.InvalidChoiceError()
