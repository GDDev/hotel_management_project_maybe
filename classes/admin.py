from classes.user import User
from classes.hotel import Hotel

# Criando uma classe específica para funcionários com maior permissionamento
class Admin(User):
    # Criando usuário admin
    def __init__(self, username, password):
        super().__init__(username, password, 'admin')

    def add_employee():
        pass
    def show_employee_info():
        pass
    def show_staff():
        pass
    def delete_employee():
        pass
