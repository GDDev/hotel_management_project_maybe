from classes.user import User

# Criando uma classe específica para funcionários com maior permissionamento
class Admin(User):
    # Criando usuário admin
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')
