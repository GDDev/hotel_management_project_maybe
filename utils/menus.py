
from utils import custom_exceptions as exp
from os import system

# Criando o menu principal
def main_menu(current_hotel, *functions):
    check_in, check_out, display_available_rooms, guests_management, random_farewell, choose_room = functions
    # Definindo as opções do menu principal
    menu = {'title': 'Menu', 
            '1. Check-in': (check_in, current_hotel, display_available_rooms, choose_room), 
            '2. Check-out': (check_out, current_hotel), 
            '3. Localizar hóspede': (guests_management, current_hotel), 
            '4. Sair': (random_farewell,)}
    return menu

# Criando menu para ADMINs
def admin_menu(current_hotel, *functions):
    check_in, check_out, display_available_rooms, guests_management, hotel_management, staff_management, random_farewell, choose_room = functions
    # Definindo opções
    menu = main_menu(current_hotel, check_in, check_out, display_available_rooms, guests_management, random_farewell, choose_room)
    del menu['4. Sair']
    admin_items = {'4. Gerenciar Hotel': (hotel_management, current_hotel), 
                    '5. Gerenciar funcionários': (staff_management, current_hotel), 
                    '6. Sair': (random_farewell,)}
    menu.update(admin_items)
    return menu

# Criando o menu de check-in
def checkin_menu(current_hotel, rooms, *functions):
    display_available_rooms, choose_room = functions
    # Definindo as opções do menu principal
    menu = {'title': 'Check-in', 
            '1. Mostrar quartos disponíveis': (display_available_rooms, rooms), 
            '2. Hospedar': (choose_room, current_hotel), 
            '3. Voltar': 'break'}
    return menu

# Criando o menu de check-out
def checkout_menu(current_hotel, chekin):
    # Definindo as opções do menu principal
    menu = {'title': 'Check-out', 
            '1. Localizar hospedagem': (chekin.get_open_checkins, current_hotel), 
            '2. Voltar': 'break'}
    return menu

def guest_checkin_menu(*functions):
    get_guest_by_name, create_guest = functions
    menu = {'title': 'Hóspede',
            '1. Hóspede já cadastrado': (get_guest_by_name,),
            '2. Cadastrar novo hóspede': (create_guest,),
            '3. Voltar': 'break'}
    return menu

# Criando menu para gerenciamento do hotel
def hotel_management_menu(current_hotel, *functions):
    display_hotels, create_hotel, update_hotel_info, delete_hotel = functions
    # Definindo opções
    menu = {'title': 'Gerenciamento do Hotel',
            '1. Visualizar todos os hotéis': (display_hotels,),
            '2. Cadastrar novo hotel': (create_hotel,),
            '3. Atualizar hotel': (update_hotel_info, current_hotel),
            '4. Excluir hotel': (delete_hotel, current_hotel),
            '5. Voltar': 'break'}
    return menu  

# Criando menu para gerenciamento de funcionários
def staff_management_menu(current_hotel, *functions):
    create_user, show_user_details, show_all_staff, eliminate_user = functions
    menu = {'title': 'Gerenciamento de Funionários', 
            '1. Adicionar funcionário': (create_user, current_hotel.hotel_id), 
            '2. Ver detalhes de um funcionáio': (show_user_details, current_hotel), 
            '3. Ver todos os funcionários': (show_all_staff,), 
            '4. Deletar um funcionário': (eliminate_user, current_hotel), 
            '5. Voltar': 'break'}
    return menu

def update_hotel_menu(current_hotel, *functions):
    add_room, create_user, edit_hotel_info = functions
    menu = {'title': 'Atualizar Hotel', 
            '1. Adicionar quarto': (add_room, current_hotel), 
            '2. Adicionar funcionário': (create_user, current_hotel.hotel_id), 
            '3. Editar Hotel': (edit_hotel_info, current_hotel), 
            '4. Voltar': 'break'}
    return menu

def guests_menus(current_hotel, *functions):
    all_guests, find_guest = functions
    menu = {'title': 'Hóspedes',
            '1. Ver todos os hóspedes': (all_guests, current_hotel),
            '2. Encontrar hóspede': (find_guest,),
            '3. Voltar': 'break'}
    return menu

def guest_management_menu(current_hotel, chosen_guest, *functions):
    menu = {'title': 'Gerenciar hóspede',
            '1. Mostrar informações completas': (chosen_guest.display_guest_info,),
            '2. Atualizar informações': (chosen_guest.edit_guest_info,),
            '3. Excluir hóspede': (chosen_guest.delete_guest, current_hotel),
            '4. Voltar': 'break'}
    return menu

def user_management_menu(current_hotel, user, *functions):
    edit_user_info, change_password = functions
    menu = {'title': '',
            '1. Atualizar funcionário': (edit_user_info, user),
            '2. Alterar senha': (change_password, user),
            '3. Voltar': 'break'}
    return menu

# Criando função para exibir o menu escolhido
def menu(menu_list, current_hotel, *functions):
    try:
        # Validando a opção escolhida
        def validate_menu_choice(length):
            while True:
                # Recebendo opção escolhida
                choice = input('Selecione uma opção: ')
                system('cls')
                int_choice = int(choice)
                # Verificando se é uma das existentes
                if int_choice in range(1, length):
                    # Opção válida é retornada
                    return choice
                raise exp.InvalidChoiceError()
        
        show_list = menu_list(current_hotel, *functions)

        for key, value in show_list.items():
            if key == 'title':
                print(value)
            else:
                print(key)
        # Recebendo número de opções do menu (não precisa descontar por causa do título)
        length = len(show_list)
        # Vendo se o usuário digitou uma opção válida
        choice = validate_menu_choice(length)
        for key, value in show_list.items():
            if key.startswith(choice):
                option = value
                break
        if option == 'break':
            return 'break'
        else:
            function, *params = option
            result = function(*params)
        if result:
            return result
    except ValueError as e:
        print('Opção inválida, tente novamente.')
        input('Pressione ENTER para continuar...')
        system('cls')
    except AttributeError as e:
        print('Opção inválida, tente novamente.')
        input('Pressione ENTER para continuar...')
        system('cls')
    except exp.InvalidChoiceError as e:
        print(e)
        input('Pressione ENTER para continuar...')
        system('cls')
