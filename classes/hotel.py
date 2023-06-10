from data.database import Database
from os import system
from classes.room import Room, RoomType
from classes.checkin import Checkin
from classes.guest import Guest
from utils import menus

# Criando classe para o hotel
class Hotel:
    def load_rooms(self):
        db = Database('hotel.db')
        rooms = Database.get_hotel_rooms(db, self.hotel_id)
        rooms_class = []
        for room in rooms:
            room_id, number, room_type, capacity, price, is_occupied, hotel_id = room
            is_occupied = False if is_occupied == 0 else True
            for type in RoomType:
                    room_type = type if room_type == type.value else room_type
            room_class = Room(room_id, number, room_type, capacity, price, hotel_id, is_occupied)
            rooms_class.append(room_class)
        return rooms_class

    def load_staff(self):
        return []
    
    def load_guests(self):
        return []

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

    def add_room(self, db):
        hotel = self
        room = Room.create_new_room(hotel)
        room_id, number, type, capacity, price, is_occupied, hotel_id = Database.insert_room(db, room)
        room = Room(room_id, number, type, capacity, price, hotel_id)
        self.rooms.append(room)

    def add_employee(self, employee):
        self.staff.append(employee)

    def create_new_hotel(db):
        name = input('Informe o nome do Hotel: ')
        address = input('Informe a rua do Hotel: ')
        city = input('Informe a cidade do Hotel: ')
        state = input('Informe o estado do Hotel: ')
        country = input('Informe o país do Hotel: ')

        hotel = (name, address, city, state, country)
        hotel_id = Database.insert_hotel(db, hotel)
        return Hotel(hotel_id, name, address, city, state, country)
    
    def checkin_guest(self, db, room):
        choice = menus.menu(menus.guest_checkin_menu)
        if choice == '1':
            pass
        elif choice == '2':
            guest = Guest.create_new_guest()
            name, last_name, email, phone = guest
            guest_id = Database.insert_guest(db, guest)
            guest = Guest(guest_id, name, last_name, email, phone)
        room.checkin_room(guest)
        Database.checkin_room(db, room.room_id)
        date = Checkin.check_in()
        checkin = (date, guest.guest_id, room.room_id, self.hotel_id)
        Database.insert_checkin(db, checkin)

    def checkout_guest(self, db, checkin_id):
        # Probably gonna need the checkin id :)
        pass

    # *** FUNÇÕES DE MANIPULAR O HOTEL ***

    def edit_hotel_info(self, db):
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
            Database.update_hotel(db, self.hotel_id, self.name, self.address, self.city, self.state, self.country)
        else:
            print('Opção inválida')
        
    def update_hotel_info(self, db):
        system('cls')
        print('Hotéis')
        choice = menus.menu(menus.update_hotel_menu)
        if choice == '1':
            self.add_room(db)
        elif choice == '2':
            pass
        elif choice == '3':
            self.edit_hotel_info(db)
        elif choice == '4':
            return

    def delete_hotel(db):
        system('cls')
        print('Hotéis')
        hotels = Hotel.display_hotels(db)
        choice = input('Qual hotel deseja excluir? ')
        int_choice = int(choice)
        if int_choice in range(1, len(hotels) + 1):
            Database.exclude_hotel(db, choice)

    # *** FUNÇÕES DE RECUPERAR OBJETOS ***

    def display_hotels(db):
        hotels = Database.get_all_hotels(db)
        hotel_list_class = []
        for hotel in hotels:
            id, name, address, city, state, country = hotel
            hotel_class = Hotel(id, name, address, city, state, country)
            print(f'{hotel_class.hotel_id}. Hotel {hotel_class.name}\n'
                  f'Localizado em {hotel_class.address}, {hotel_class.city}-{hotel_class.state}, {hotel_class.country}\n')
            hotel_list_class.append(hotel_class)
        return hotel_list_class
    
    def display_all_rooms(self):
        counter = 1
        for room in self.rooms:
            if room.is_occupied == False:
                print(f'{counter}. Quarto {room.number}, tipo: {room.type.value}, capacidade: {room.capacity}, preço por noite: R$ {room.price:.2f}')
                counter += 1

    def display_all_staff(self):
        return self.staff
