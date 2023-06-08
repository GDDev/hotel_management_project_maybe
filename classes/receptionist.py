from classes.user import User

# Criando classe específica para funcionários com poucas permissões
class Receptionist(User):
    # Criando funcionário comum
    def __init__(self, username, password):
        super().__init__(username, password)
