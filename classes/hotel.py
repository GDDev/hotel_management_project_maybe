from globals import db_name
from os import system
from classes.room import Room
from classes.checkin import CheckIn
from classes.guest import Guest
from classes.user import User
from data.hotel_database import HotelDatabase
from utils import menus
from utils import custom_exceptions

DB = HotelDatabase(db_name)

# Criando classe para o hotel
class Hotel:

    def load_rooms(self):
        return Room.get_all_rooms(self.hotel_id)

    def load_staff(self):
        return User.get_all_users(self.hotel_id)
    
    def load_guests(self):
        return Guest.get_all_guests()

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
    
    # *** FUNÇÕES DE ADICIONAR OBJETOS ***

    def add_room(self):
        room = Room.create_room(Room, self.hotel_id)
        self.rooms.append(room)

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
    
    def checkin_guest(self, room):
        choice = menus.menu(menus.guest_checkin_menu)
        if choice == '1':
            guest_list = Guest.get_all_guests()
            if guest_list:
                for gst in guest_list:
                    print(f'{gst.name} {gst.last_name} - ID: {gst.guest_id}')
            else:
                print('Nenhum hóspede cadastrado.')
            guest = Guest.get_guest_by_name()
            if not guest:
                print('Nenhum hóspede correspondente à pesquisa.')
                choice = '2'
        if choice == '2':
            guest = Guest.create_guest()
        check_in = CheckIn.check_in(CheckIn, guest.guest_id, room.room_id, self.hotel_id)
        room.checkin_room()
        print('Check-in realizado com sucesso!')

    def checkout_guest(self):
        checkins = CheckIn.get_open_checkins(CheckIn, self.hotel_id)
        rooms = Room.display_occupied_rooms(Room, self.hotel_id)
        if rooms:
            choice = input('Informe o número do quarto para realizar o check-out: ')
            int_choice = int(choice)
            for room in rooms:
                if int_choice == room.number:
                    chosen_room = room
                    for checkin in checkins:
                        if checkin.room_id == chosen_room.room_id:
                            check = checkin
                            debt = chosen_room.checkout_room()
                            nights = check.check_out()
                            debt = CheckIn.calculate_debt(nights, debt)
                            print(f'Total a cobrar: R$ {debt:.2f}\n')
        else:
            print('Nenhum quarto está ocupado no momento.\n')


    # *** FUNÇÕES DE MANIPULAR O HOTEL ***

    def edit_hotel_info(self):
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
                f'1. Nome = {self.name}',
                f'2. Rua = {self.address}',
                f'3. Cidade = {self.city}',
                f'4. Estado = {self.state}',
                f'5. País = {self.country}']
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
                self.name = change_hotel_name()
            elif choice == '2':
                self.address = change_hotel_address()
            elif choice == '3':
                self.city = change_hotel_city()
            elif choice == '4':
                self.state = change_hotel_state()
            elif choice == '5':
                self.country = change_hotel_country()
            DB.update_hotel(self)
        else:
            print('Opção inválida')
        
    def update_hotel_info(self):
        system('cls')
        print('Hotéis')
        choice = menus.menu(menus.update_hotel_menu)
        if choice == '1':
            self.add_room()
        elif choice == '2':
            pass
        elif choice == '3':
            self.edit_hotel_info()
        elif choice == '4':
            return

    def delete_hotel():
        if len(DB.get_all_hotels()) == 1:
            print('Não é possível deletar o único hotel cadastrado.')
            return
        system('cls')
        print('Hotéis')
        hotels = Hotel.display_hotels()
        choice = input('Qual hotel deseja excluir? ')
        int_choice = int(choice)
        if int_choice in range(1, len(hotels) + 1):
            DB.exclude_hotel(choice)

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
        return hotel_list_class

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
            raise custom_exceptions.InvalidChoiceError('Hotel inválido.')
