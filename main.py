# Importando tudo o que vai usar
from classes.hotel import Hotel
from classes.user import Admin, User
from data.database import Database
from data.hotel_database import HotelDatabase
from globals import db_name
from os import system, path
from utils.menus import admin_menu, main_menu, menu
from utils.farewell import random_farewell 
from utils.custom_exceptions import InvalidChoiceError, LoginError
from classes.checkin import CheckIn
from classes.guest import Guest
from classes.room import Room

def main():
    
    # Checando se o arquivo do Banco de Dados existe
    if not path.isfile('hotel.db'):
        # Criando um Banco de Dados
        DB = Database(db_name)
        # Executando a função de inicialização do bd e recebendo o usuário e hotel criados
        user, hotel = DB.initialize(Hotel.create_hotel, User.create_user)
        # Definindo o hotel criado como o atual
        current_hotel = hotel
        # Definindo o usuário criado como logado
        logged_user = user
    else:
        # Iniciando o laço de login
        while True:
            try:
                # Criando um Banco de Dados com as funções de manipulação da classe Hotel
                DB = HotelDatabase(db_name)
                # Verificando os hotéis existentes
                hotels = DB.get_all_hotels()
                # Caso haja mais de um hotel, o usuário deverá escolher um
                if len(hotels) > 1:
                    # Chamando função para escolher um hotel e atribuindo o resultado ao hotel atual
                    current_hotel = Hotel.choose_hotel()
                else:
                    # Recebendo as variáveis do único hotel
                    hotel_id, name, address, city, state, country = hotels[0]
                    # Definindo o único hotel existente como o atual
                    current_hotel = Hotel(hotel_id, name, address, city, state, country)
                # Chamando a função de login e atribuindo o resultado ao usuário logado
                logged_user = User.perform_login(User)
                break
            except ValueError as e:
                system('cls')
                print('ID do Hotel deve ser um número inteiro.')
                input('\nPressione ENTER para tentar novamente.')
            except InvalidChoiceError as e:
                system('cls')
                print(e)
                input('\nPressione ENTER para tentar novamente.')
            except LoginError as e:
                system('cls')
                print(e)
                break
    while True:
        try:
            # Verificando o tipo de usuário logado
            if isinstance(logged_user, Admin):
                system('cls')
                # Exibindo o menu principal para admins
                result = menu(admin_menu, current_hotel, CheckIn.check_in, CheckIn.check_out, Room.display_available_rooms, Guest.guests_management, Hotel.hotel_management, User.staff_management, random_farewell, Room.choose_room)
                if result:
                    print(result)
                    break
            else:
                # Exibindo o menu principal para recepcionistas
                result = menu(main_menu, current_hotel, CheckIn.check_in, CheckIn.check_out, Room.display_available_rooms, Guest.guests_management, random_farewell, Room.choose_room)
                if result:
                    # Encerrando o programa
                    print(result)
                    break
        except UnboundLocalError as e:
            system('cls')
            print('Impossível iniciar o programa.')
            break
        except ValueError as e:
            # print('Opção inválida, tente novamente.')
            print(e)
            input('\nPressione ENTER para tentar novamente.')
        except InvalidChoiceError as e:
            print(e)
            input('\nPressione ENTER para tentar novamente.')

# Iniciando o programa
if __name__ == '__main__':
        main()
