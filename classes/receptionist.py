from classes.user import User

# Criando classe específica para funcionários com poucas permissões
class Receptionist(User):
    # Criando funcionário comum
    def __init__(self, user_id, username, password, hotel_id, role='receptionist'):
        super().__init__(user_id, username, password, hotel_id, role)
