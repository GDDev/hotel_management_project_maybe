# Criando classe para os hóspedes
class Guest:
    # Definindo atributos padrão
    def __init__(self, name, mid_name, last_name, email, phone):
        self.name = name
        self.middle_name = mid_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.history = []
