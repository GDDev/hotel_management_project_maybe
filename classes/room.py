from globals import db_name
from enum import Enum
from os import system
from utils.custom_exceptions import RoomTypeError, InvalidChoiceError
from data.room_database import RoomDatabase

DB = RoomDatabase(db_name)

class RoomType(Enum):
    SOLTEIRO = 'Solteiro'
    CASAL = 'Casal'
    MASTER = 'Master'

# Criando classe para os quartos
class Room:
    # Definindo os atributos padrão dos quartos
    def __init__(self, id, number, room_type, capacity, price, hotel_id, is_occupied=False):
        self.room_id = id
        self.number = number
        self.type = room_type
        self.capacity = capacity
        self.price = price
        self.is_occupied = is_occupied
        self.hotel = hotel_id

        if not isinstance(self.type, RoomType):
            raise RoomTypeError()

    def create_room(self, hotel_id):
        rooms = self.get_all_rooms(hotel_id)

        room_number = input('Informe o número do novo quarto: ')
        if room_number not in rooms:
            for type in RoomType:
                print(type.value)
            room_type = RoomType.SOLTEIRO
            type_choice = input('Escolha o tipo de quarto: ')
            for type in RoomType:
                if type.value.lower() == type_choice.lower():
                    room_type = type
                    break 
            room_capacity = input('Informe a capacidade do quarto: ')
            int_capacity = int(room_capacity)
            room_price = input('Informe o preço - por noite - do quarto: R$ ')
            float_price = float(room_price)

            room = (room_number, room_type, int_capacity, float_price, False, hotel_id)
            room_id = DB.insert_room(room)
            room = Room(room_id, room_number, room_type, int_capacity, float_price, False, hotel_id)
            return room
        else:
            print(f'Quarto {room_number} já existe.')
        
    def get_all_rooms(hotel_id):
        rooms = DB.get_hotel_rooms(hotel_id)
        room_list = []
        for room in rooms:
            room_id, number, room_type, capacity, price, is_occupied, hotel_id = room
            is_occupied = False if is_occupied == 0 else True
            for type in RoomType:
                    room_type = type if room_type == type.value else room_type
            room_class = Room(room_id, number, room_type, capacity, price, hotel_id, is_occupied)
            room_list.append(room_class)
        return room_list
    
    def get_available_rooms(current_hotel):
        available_rooms = []
        room_list = current_hotel.rooms
        for room in room_list:
            if room.is_occupied == False:
                available_rooms.append(room)
        return available_rooms
    
    def get_occupied_rooms(current_hotel):
        occupied_rooms = []
        room_list = current_hotel.rooms
        for room in room_list:
            if room.is_occupied == True:
                occupied_rooms.append(room)
        return occupied_rooms

    def get_room(room_id):
        room = DB.get_room_by_id(room_id)
        room_id, number, room_type, capacity, price, is_occupied, hotel_id = room
        is_occupied = False if is_occupied == 0 else True
        for type in RoomType:
            room_type = type if room_type == type.value else room_type
        room = Room(room_id, number, room_type, capacity, price, hotel_id, is_occupied)
        return room

    def checkin_room(self):
        self.is_occupied = True
        DB.checkin_room(self.room_id)

    def checkout_room(self):
        self.is_occupied = False
        DB.checkout_room(self.room_id)
        return self.price

    def display_available_rooms(rooms):
        for room in rooms:
            print(f'Quarto {room.number}, tipo: {room.type.value}, capacidade: {room.capacity}, preço por noite: R$ {room.price:.2f}')
        if rooms == []:
            print('Nenhum quarto disponível.')
        input('\nPressione ENTER para continuar...')
        system('cls')

    def display_occupied_rooms(rooms):
        for room in rooms:
            print(f'Quarto {room.number}, tipo: {room.type.value}, capacidade: {room.capacity}, preço por noite: R$ {room.price:.2f}')


    def choose_room(current_hotel):
        system('cls')
        rooms = Room.get_available_rooms(current_hotel)
        if rooms:
            Room.display_available_rooms(rooms)
            choice = input('Escolha o quarto: ')
            int_choice = int(choice)
            for room in rooms:
                if int_choice == room.number:
                    chosen_room = room
                    return chosen_room
            raise InvalidChoiceError('Quarto inválido.')
        print('Nenhum quarto disponível.')
        input('\nPressione ENTER para continuar...')
        system('cls')
