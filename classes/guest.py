# Criando classe para os hóspedes
class Guest:
    def load_stay_history(self):
        return []

    # Definindo atributos padrão
    def __init__(self, id, name, last_name, email, phone):
        self.guest_id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.history = self.load_stay_history()

    def create_new_guest():
        full_name = input('Nome completo: ').split(' ')
        name = full_name[0]
        last_name = full_name[1:len(full_name)]
        last_name = ' '.join(last_name)
        email = input('E-mail: ')
        phone = input('Número de telefone: ')
        return (name, last_name, email, phone)

    def add_stay_to_history():
        pass
