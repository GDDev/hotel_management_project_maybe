# Criando classe para os quartos
class Room:
    # Definindo os atributos padrão dos quartos
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guest = None


    # def add_room(self, room_number, capacity):
    #     if room_number not in self.rooms:
    #         room = Room(room_number, capacity)
    #         self.rooms[room_number] = room
    #         print(f'Room {room_number} added successfully.')
    #     else:
    #         print(f'Room {room_number} already exists.')

    # def check_in(self, guest):
    #     if self.guest is None:
    #         self.guest = guest
    #         print(f"Guest {guest.name} checked into Room {self.number}.")
    #     else:
    #         print(f"Room {self.number} is already occupied.")

    # def check_out(self):
    #     if self.guest is not None:
    #         guest_name = self.guest.name
    #         self.guest = None
    #         print(f"Guest {guest_name} checked out from Room {self.number}.")
    #     else:
    #         print(f"Room {self.number} is not occupied.")
