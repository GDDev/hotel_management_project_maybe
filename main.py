# Importando tudo o que vai usar
from globals import db_name
from os import system, path
from classes.hotel import Hotel
from classes.guest import Guest 
from classes.room import Room
from classes.user import User, Admin
from data.database import Database
from utils.menus import admin_menu, checkin_menu, checkout_menu, guest_checkin_menu, hotel_management_menu, main_menu, menu, staff_management_menu, update_hotel_menu, guests_menus, guest_management_menu
from utils.farewell import random_farewell 
from utils import custom_exceptions
    
def check_in():
    while True:
        try:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            choice = menu(checkin_menu)
            if choice == '1':
                Room.display_all_rooms(Room, current_hotel.hotel_id)
                input('Pressione Enter para voltar...')
            elif choice == '2':
                room = Room.choose_room(Room, current_hotel.hotel_id)
                if room:
                    current_hotel.checkin_guest(room)
                input('Pressione Enter para voltar...')
            elif choice == '3':
                break
        except ValueError as e:
            pass
        except AttributeError as e:
            print('Função não implementada.')
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

def check_out():
    while True:
        try:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            choice = menu(checkout_menu)
            if choice == '1':
                current_hotel.checkout_guest()
                input('Pressione Enter para voltar...')
            elif choice == '2':
                break
        except ValueError as e:
            pass
        except AttributeError as e:
            print('Função não implementada.')
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

def hotel_management():
    while True:
        try:
            # Chamando o menu e recebendo a opção escolhida
            choice = menu(hotel_management_menu)
            if choice == '1':
                Hotel.display_hotels()
                input('Pressione Enter para voltar...')
                system('cls')
            elif choice == '2':
                Hotel.create_hotel()
                input('Pressione Enter para voltar...')
                system('cls')
            elif choice == '3':
                current_hotel.update_hotel_info()
                input('Pressione Enter para voltar...')
                system('cls')
            elif choice == '4':
                Hotel.delete_hotel()
                input('Pressione Enter para voltar...')
                system('cls')
            elif choice == '5':
                break
        except ValueError as e:
            print(e)
        except AttributeError as e:
            print('Função não implementada.')
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

# Função para gerenciamento de funcionários
def staff_management():
    while True:
        system('cls')
        try:
            # Chamando o menu e recebendo a opção escolhida
            choice = menu(staff_management_menu)
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
        except ValueError as e:
            pass
        except AttributeError as e:
            print('Função não implementada.')
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

def guests_management():
    while True:
        try:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            choice = menu(guests_menus)
            if choice == '1':
                guests = current_hotel.display_all_guests()
                choice = input('informe o ID do hóspede: ')
                int_choice = int(choice)
                for guest in guests:
                    if guest.guest_id == int_choice:
                        chosen_guest = guest                
            elif choice == '2':
                raise AttributeError()
                input('Pressione Enter para voltar...')
                system('cls')
            elif choice == '3':
                break
            if chosen_guest:
                    system('cls')
                    choice = menu(guest_management_menu)
                    if choice == '1':
                        chosen_guest.display_guest_info()
                    elif choice == '2':
                        chosen_guest.edit_guest_info()
                    elif choice == '3':
                        chosen_guest.delete_guest(current_hotel)
                    elif choice == '4':
                        break
        except ValueError as e:
            print(e)
        except AttributeError as e:
            print('Função não implementada.')
            print(e)
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

# Definindo o escopo principal
def main():

    while True:
        try:
            # Exibindo o menu principal
            if isinstance(logged_user, Admin):
                system('cls')
                # Chamando o menu e recebendo a opção escolhida
                choice = menu(admin_menu)

                if choice == '1':
                    check_in()
                elif choice == '2':
                    check_out()
                elif choice == '3':
                    Room.display_all_rooms(Room, current_hotel.hotel_id)
                    input('Pressione Enter para voltar...')
                    system('cls')
                elif choice == '4':
                    guests_management()
                elif choice == '5':
                    hotel_management()
                elif choice == '6':
                    staff_management()
                elif choice == '7':
                    # Encerrando o programa
                    print(random_farewell())
                    break
            else:
                # Chamando o menu e recebendo a opção escolhida
                choice = menu(main_menu)

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
        except ValueError as e:
            pass
        except AttributeError as e:
            print('Função não implementada.')
            input('Pressione Enter para voltar...')
        except custom_exceptions.InvalidChoiceError as e:
            print(e)
            input('Pressione Enter para voltar...')

DB = Database(db_name)

# Iniciando o programa
if __name__ == '__main__':
    try:
        if not path.isfile('hotel.db'):
            # Executando a função de inicialização do bd
            user, hotel = DB.initialize(Hotel.create_hotel, User.create_user)
            current_hotel = hotel
            logged_user = user
        else:
            # Executando o login
            # current_hotel = Hotel.choose_hotel()
            # logged_user = User.perform_login(User, current_hotel.hotel_id)
            current_hotel = Hotel(1, 'Hotel', 'Rua', 'Cidade', 'Estado', 'País')
            logged_user = Admin(1, 'Jorge', 'Inho', 'email', 'god', '1', 'admin', 1)
        # Executando o programa
        main()
    except custom_exceptions.LoginError as e:
        system('cls')
        print(e)
    except custom_exceptions.InvalidChoiceError as e:
        system('cls')
        print(e)
