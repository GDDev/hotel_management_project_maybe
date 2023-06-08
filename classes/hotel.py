from classes.guest import Guest
from classes.room import Room

# Criando classe para o hotel
class Hotel:
    # Definindo atributos iniciais
    def __init__(self):
        self.rooms = {}

    # Criando função para definir o nome do hotel
    def set_hotel_name(self, name):
        setattr(self, 'name', name)
    # Criando função para definir o endereço (rua) do hotel
    def set_hotel_address(self, address):
        setattr(self, 'address', address)
    # Criando função para definir a cidade do hotel
    def set_hotel_city(self, city):
        setattr(self, 'city', city)
    # Criando função para definir o estado do hotel
    def set_hotel_state(self, state):
        setattr(self, 'state', state)
    # Criando função para definir o país do hotel
    def set_hotel_country(self, country):
        setattr(self, 'country', country)
    

    # def check_in(self, room_number, guest_name):
    #     if room_number in self.rooms:
    #         room = self.rooms[room_number]
    #         room.check_in(Guest(guest_name))
    #     else:
    #         print(f'Room {room_number} does not exist.')

    # def check_out(self, room_number):
    #     if room_number in self.rooms:
    #         room = self.rooms[room_number]
    #         room.check_out()
    #     else:
    #         print(f'Room {room_number} does not exist.')

    # def display_guests(self):
    #     print('Occupied Rooms:')
    #     for room_number, room in self.rooms.items():
    #         if room.guest:
    #             print(f'Room {room_number}: {room.guest.name}')
