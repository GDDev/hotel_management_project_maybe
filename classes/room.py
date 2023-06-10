from enum import Enum
from utils.custom_exceptions import RoomTypeError

class RoomType(Enum):
    SOLTEIRO = 'Solteiro'
    CASAL = 'Casal'
    MASTER = 'Master'

# Criando classe para os quartos
class Room:
    # Definindo os atributos padrão dos quartos
    def __init__(self, number, room_type, capacity, price, hotel_id):
        self.number = number
        self.type = room_type
        self.capacity = capacity
        self.price = price
        self.guest = None
        self.is_occupied = False
        self.hotel = hotel_id

        if not isinstance(self.type, RoomType):
            raise RoomTypeError()

    def create_new_room(hotel):
        room_number = input('Informe o número do novo quarto: ')
        if room_number not in hotel.rooms:
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
            room_price = input('Informe o preço - por noite - do quarto: R$')
            float_price = float(room_price)
            room = Room(room_number, room_type, int_capacity, float_price, hotel.hotel_id)
            return room
        else:
            print(f'Quarto {room_number} já existe.')

    def checkin_room(self, guest):
        self.guest = guest
        self.is_occupied = True
