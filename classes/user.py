# Criando uma classe pai para os tipos de funcionário
class User:
    # Definindo os atributos comuns
    def __init__(self, username, password, role = 'guest'):
        self.username = username
        self.password = password
        self.role = role

    # Criando função para realizar check-in
    def check_in_guest(self, hotel):
        room_number = input("Enter room number: ")
        guest_name = input("Enter guest name: ")
        hotel.check_in(room_number, guest_name)

    # Criando função para realizar check-out
    def check_out_guest(self, hotel):
        room_number = input("Enter room number: ")
        hotel.check_out(room_number)

# Criando uma classe específica para funcionários com maior permissionamento
class Admin(User):
    # Criando usuário admin
    def __init__(self, username, password):
        super().__init__('admin', 'password', 'admin')

    # Criando função para alterar o nome do hotel
    def define_hotel_name(self, hotel):
        new_name = input("Enter the hotel's new name: ")
        hotel.set_hotel_name(new_name)

    # Criando função para alterar os quartos
    def update_room_specs(self, hotel):
        room_number = input("Enter the room number: ")
        room_specs = input("Enter the new room specifications: ")
        hotel.update_room_specs(room_number, room_specs)

# Criando classe específica para funcionários com poucas permissões
class Employee(User):
    # Criando funcionário comum
    def __init__(self, username, password):
        super().__init__('employee', '123', 'employee')
