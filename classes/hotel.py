from globals import db_name
from os import system
from classes.room import Room
from classes.user import User
from classes.checkin import CheckIn
from classes.guest import Guest
from data.hotel_database import HotelDatabase
from utils.menus import hotel_management_menu, menu, update_hotel_menu
from utils.custom_exceptions import InvalidChoiceError

DB = HotelDatabase(db_name)

# Criando classe para o hotel
class Hotel:

    def load_rooms(self):
        return Room.get_all_rooms(self.hotel_id)

    def load_staff(self):
        return User.get_all_users()
    
    def load_guests(self):
        return Guest.get_all_guests()
    
    def refresh_hotel(self):
        self.rooms = self.load_rooms()
        self.staff = self.load_staff()
        self.guests = self.load_guests()


    # Definindo atributos iniciais
    def __init__(self, id, name, address, city, state, country):
        self.hotel_id = id
        self.rooms = self.load_rooms()
        self.staff = self.load_staff()
        self.guests = self.load_guests()
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country   

    def hotel_management(current_hotel):
        while True:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            result = menu(hotel_management_menu, current_hotel, Hotel.display_hotels, Hotel.create_hotel, Hotel.update_hotel_info, Hotel.delete_hotel)
            if result == 'break':
                break
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    # *** FUNÇÕES DE ADICIONAR OBJETOS ***

    def add_room(self):
        Room.create_room(Room, self.hotel_id)
        self.refresh_hotel()

    def add_employee(self):
        user = User.create_user(self.hotel_id)
        self.staff.append(user)

    def create_hotel():
        name = input('Informe o nome do Hotel: ')
        address = input('Informe a rua do Hotel: ')
        city = input('Informe a cidade do Hotel: ')
        state = input('Informe o estado do Hotel: ')
        country = input('Informe o país do Hotel: ')

        hotel = (name, address, city, state, country)
        hotel_id = DB.insert_hotel(hotel)
        return Hotel(hotel_id, name, address, city, state, country)

    # *** FUNÇÕES DE MANIPULAR O HOTEL ***

    def edit_hotel_info(current_hotel):
        def change_hotel_name():
            name = input('Informe o novo nome do Hotel: ')
            return name
        def change_hotel_address():
            address = input('Informe a nova rua do Hotel: ')
            return address
        def change_hotel_city():
            city = input('Informe a nova cidade do Hotel: ')
            return city
        def change_hotel_state():
            state = input('Informe o novo estado do Hotel: ')
            return state
        def change_hotel_country():
            country = input('Informe o novo país do Hotel: ')
            return country
        
        menu = ['Alterar informação',
                f'1. Nome = {current_hotel.name}',
                f'2. Rua = {current_hotel.address}',
                f'3. Cidade = {current_hotel.city}',
                f'4. Estado = {current_hotel.state}',
                f'5. País = {current_hotel.country}']
        system('cls')
        # Exibindo o menu
        for line in menu:
            print(line)
        # Recebendo número de opções do menu (não precisa descontar por causa do título)
        length = len(menu)
        choice = input('Selecione uma opção: ')
        # Vendo se o usuário digitou uma opção válida
        if int(choice) in range(1, length):
            system('cls')
            if choice == '1':
                current_hotel.name = change_hotel_name()
            elif choice == '2':
                current_hotel.address = change_hotel_address()
            elif choice == '3':
                current_hotel.city = change_hotel_city()
            elif choice == '4':
                current_hotel.state = change_hotel_state()
            elif choice == '5':
                current_hotel.country = change_hotel_country()
            DB.update_hotel(current_hotel)
        else:
            print('Opção inválida')
        
    def update_hotel_info(current_hotel):
        system('cls')
        print('Hotéis')
        menu(update_hotel_menu, current_hotel, Hotel.add_room, User.create_user, Hotel.edit_hotel_info)

    def delete_hotel(current_hotel):
        if len(DB.get_all_hotels()) == 1:
            system('cls')
            print('Não é possível deletar o único hotel cadastrado.')
        else:
            system('cls')
            print('Hotéis')
            hotels = Hotel.display_hotels()
            choice = input('Qual hotel deseja excluir? ')
            int_choice = int(choice)
            if int_choice in range(1, len(hotels) + 1):
                if current_hotel.hotel_id == int_choice:
                    system('cls')
                    print('Não é possível deletar um hotel em funcionamento!')
                else:
                    DB.exclude_hotel(choice)
                    print('Hotel deletado!')
        input('\nPressione ENTER para continuar...')
        system('cls')

    # *** FUNÇÕES DE RECUPERAR OBJETOS ***

    def display_hotels():
        hotels = DB.get_all_hotels()
        hotel_list_class = []
        for hotel in hotels:
            id, name, address, city, state, country = hotel
            hotel_class = Hotel(id, name, address, city, state, country)
            print(f'{hotel_class.hotel_id}. Hotel {hotel_class.name}\n'
                  f'Localizado em {hotel_class.address}, {hotel_class.city}-{hotel_class.state}, {hotel_class.country}\n')
            hotel_list_class.append(hotel_class)
        input('\nPressione ENTER para continuar...')
        return hotel_list_class
    
    def get_hotel_by_id(hotel_id):
        hotel = DB.get_hotel_by_id(hotel_id)
        hotel_id, name, address, city, state, country = hotel
        hotel = Hotel(hotel_id, name, address, city, state, country)
        return hotel
    
    def display_all_guests(self):
        for guest in self.guests:
            print(f'{guest.guest_id}. {guest.name} {guest.last_name}')
        return self.guests

    def display_all_staff(self):
        return self.staff
    
    def choose_hotel():
        system('cls')
        hotels = Hotel.display_hotels()
        choice = input('Escolha um hotel: ')
        int_choice = int(choice)
        if int_choice in range(1, len(hotels) + 1):
            chosen_hotel = hotels[int_choice - 1]
            system('cls')
            return chosen_hotel
        else:
            raise InvalidChoiceError('Hotel inválido.')
        
        
