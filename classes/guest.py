from globals import db_name
from data.guest_database import GuestDatabase
from classes.checkin import CheckIn

DB = GuestDatabase(db_name)

# Criando classe para os hóspedes
class Guest:
    def load_stay_history(self):
        checkin_history = CheckIn.get_guest_history(CheckIn, self.guest_id)
        return checkin_history

    # Definindo atributos padrão
    def __init__(self, id, name, last_name, email, phone):
        self.guest_id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.history = self.load_stay_history()

    def create_guest():
        full_name = input('Nome completo: ').split(' ')
        name = full_name[0]
        last_name = full_name[1:len(full_name)]
        last_name = ' '.join(last_name)
        email = input('E-mail: ')
        phone = input('Número de telefone: ')
        guest = (name.upper(), last_name.upper(), email, phone)
        guest_id = DB.insert_guest(guest)
        guest = Guest(guest_id, name, last_name, email, phone)
        return guest

    def get_all_guests():
        guest_list = []
        guests = DB.get_all_guests()
        for guest in guests:
            guest_id, name, last_name, email, phone = guest
            guest_class = Guest(guest_id, name, last_name, email, phone)
            guest_list.append(guest_class)
        return guest_list
    
    def get_guest_by_name():
        guest_name = input('Digite o nome do hóspede: ')
        guests = DB.get_guest_by_name(guest_name)
        guest_list = []
        if guests:
            for guest in guests:
                guest_id, name, last_name, email, phone = guest
                guest_class = Guest(guest_id, name, last_name, email, phone)
                guest_list.append(guest_class)
                print(f'{name} {last_name} - ID: {guest_id}')
            choice = input('Digite o ID do hóspede desejado: ')
            int_choice = int(choice)
            for guest in guest_list:
                if int_choice == guest.guest_id:
                    return guest
        return []

    def add_stay_to_history(self, checkin):
        self.history.append(checkin)
