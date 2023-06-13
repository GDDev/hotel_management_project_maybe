from os import system
from globals import db_name
from data.guest_database import GuestDatabase
from classes.checkin import CheckIn
from utils.custom_exceptions import InvalidInputError
from utils.menus import guest_management_menu, guests_menus, menu
from utils.validate_input import validate_email, validate_name

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


    def all_guests(current_hotel):
        guests = current_hotel.display_all_guests()
        print('0. Voltar')
        choice = input('informe o ID do hóspede: ')
        int_choice = int(choice)
        if int_choice == 0:
            return None
        for guest in guests:
            if guest.guest_id == int_choice:
                chosen_guest = guest
                return chosen_guest
        system('cls')

    def find_guest():
        chosen_guest = Guest.get_guest_by_name()
        if not chosen_guest:
            print('Hóspede não encontrado')
            input('Pressione Enter para voltar...')
        system('cls')
        return chosen_guest

    def guests_management(current_hotel):
        while True:
            system('cls')
            # Chamando o menu e recebendo a opção escolhida
            chosen_guest = menu(guests_menus, current_hotel, Guest.all_guests, Guest.find_guest)
            if chosen_guest == 'break':
                break
            if chosen_guest:
                system('cls')
                result = menu(guest_management_menu, current_hotel, chosen_guest, chosen_guest.display_guest_info, chosen_guest.edit_guest_info)
                if result:
                    print(result)
                    break

    def create_guest():
        try:
            full_name = input('Nome completo: ')
            name, last_name = validate_name(full_name)
            email = input('E-mail: ')
            validate_email(email)
            phone = input('Número de telefone: ')
            guest = (name.upper(), last_name.upper(), email, phone)
            guest_id = DB.insert_guest(guest)
            guest = Guest(guest_id, name.capitalize(), last_name.title(), email, phone)
            return guest
        except InvalidInputError as e:
            print(e)
            input('Pressione ENTER para voltar...')
            system('cls')

    def get_all_guests():
        guest_list = []
        guests = DB.get_all_guests()
        for guest in guests:
            guest_id, name, last_name, email, phone = guest
            guest_class = Guest(guest_id, name, last_name, email, phone)
            guest_list.append(guest_class)
        return guest_list
    
    def get_guest_by_name():
        print('0. Voltar')
        guest_name = input('Digite o nome do hóspede: ')
        if guest_name == '0':
            return None
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
    
    def display_guest_info(self):
        from classes.hotel import Hotel
        from classes.room import Room

        print(f'{self.name} {self.last_name} - ID {self.guest_id}')
        print(f'E-mail: {self.email}')
        print(f'Número de contato: {self.phone}')
        print('Histórico de hospedagem:')
        if self.history:
            for check in self.history:
                # checkin_id, checkin_date, checkout_date, guest_id, room_id, hotel_id
                hotel_info = Hotel.get_hotel_by_id(check.hotel_id)
                room = Room.get_room(check.room_id)
                check_in = check.checkin_date.date()
                check_out = check.checkout_date
                if check_out:
                    check_out = check.checkout_date.date()
                else:
                    check_out = 'N/A'
                print(f'{check.checkin_id}. Data: {check_in} - {check_out}. Quarto {room.number}, Hotel {hotel_info.name}')
        else:
            print('Hóspede não possue histórico.')
        input('\nPressione Enter para voltar...')
        system('cls')

    def add_stay_to_history(self, checkin):
        self.history.append(checkin)

    def edit_guest_info(self):
        def change_guest_name():
            name = input('Informe o novo nome do Hóspede: ')
            return name
        def change_guest_last_name():
            last_name = input('Informe o novo sobrenome do Hóspede: ')
            return last_name
        def change_guest_email():
            email = input('Informe o novo e-mail do hóspede: ')
            return email
        def change_guest_phone():
            phone = input('Informe o novo número de telefone do Hóspede: ')
            return phone
        
        menu = ['Alterar informação',
                f'1. Nome = {self.name}',
                f'2. Sobrenome = {self.last_name}',
                f'3. E-mail = {self.email}',
                f'4. Número de telefone = {self.phone}',
                '5. Voltar']
        system('cls')
        # Exibindo o menu
        for line in menu:
            print(line)
        # Recebendo número de opções do menu (não precisa descontar por causa do título)
        length = len(menu)
        choice = input('Selecione uma opção: ')
        # Vendo se o usuário digitou uma opção válida
        if int(choice) in range(1, length):
            system('cls')
            if choice == '1':
                self.name = change_guest_name()
            elif choice == '2':
                self.last_name = change_guest_last_name()
            elif choice == '3':
                self.email = change_guest_email()
            elif choice == '4':
                self.phone = change_guest_phone()
            elif choice == '5':
                return self
            DB.update_guest(self)
        else:
            print('Opção inválida')

    def delete_guest(self, hotel):
        DB.delete_guest(self.guest_id)
        hotel.remove_guest(self)
