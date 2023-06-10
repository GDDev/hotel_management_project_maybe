# Criando uma classe pai para os tipos de funcionário
class User:
    # Definindo os atributos comuns
    def __init__(self, id, username, password, hotel_id, role):
        self.user_id = id
        self.username = username
        self.password = password
        self.role = role
        self.hotel = hotel_id

    def checkin_guest():
        pass
    def checkout_guest():
        pass
    def display_available_rooms():
        pass
    def display_occupied_room_info():
        pass
