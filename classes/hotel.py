from data.database import Database
from os import system
# Criando classe para o hotel
class Hotel:
    # Definindo atributos iniciais
    def __init__(self, name, address, city, state, country):
        self.rooms = {}
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.country = country    

    def display_hotels(db):
        hotels = Database.get_all_hotels(db)
        for hotel in hotels:
            id, name, address, city, state, country = hotel
            print(f'{id}. Hotel {name}\n'
                  f'Localizado em {address}, {city}-{state}, {country}\n')
        return hotels

    def create_new_hotel(db):
        name = input('Informe o nome do Hotel: ')
        address = input('Informe a rua do Hotel: ')
        city = input('Informe a cidade do Hotel: ')
        state = input('Informe o estado do Hotel: ')
        country = input('Informe o país do Hotel: ')

        hotel = (name, address, city, state, country)
        Database.insert_hotel(db, hotel)

    def update_hotel_info(db):
        def change_hotel_name():
            name = input('Informe o novo nome do Hotel: ')
            return name
        def change_hotel_address():
            address = input('Informe a nova rua do Hotel: ')
            return address
        def change_hotel_city():
            city = input('Informe a nova cidade do Hotel: ')
            return city
        def change_hotel_state():
            state = input('Informe o novo estado do Hotel: ')
            return state
        def change_hotel_country():
            country = input('Informe o novo país do Hotel: ')
            return country

        system('cls')
        print('Hotéis')
        hotels = Hotel.display_hotels(db)
        choice = input('Qual hotel deseja alterar? ')
        int_choice = int(choice)
        if int_choice in range(1, len(hotels) + 1):
            hotel = hotels[int_choice - 1]
            hotel_id, name, address, city, state, country = hotel
            menu = ['Alterar informação',
                    f'1. Nome = {name}',
                    f'2. Rua = {address}',
                    f'3. Cidade = {city}',
                    f'4. Estado = {state}',
                    f'5. País = {country}']
            system('cls')
            # Exibindo o menu
            for line in menu:
                print(line)
            # Recebendo número de opções do menu (não precisa descontar por causa do título)
            length = len(menu)
            choice = input('Selecione uma opção: ')
            # Vendo se o usuário digitou uma opção válida
            if int(choice) in range(1, length):
                if choice == '1':
                    name = change_hotel_name()
                elif choice == '2':
                    address = change_hotel_address()
                elif choice == '3':
                    city = change_hotel_city()
                elif choice == '4':
                    state = change_hotel_state()
                elif choice == '5':
                    country = change_hotel_country()
                Database.update_hotel(db, hotel_id, name, address, city, state, country)
            else:
                print('Opção inválida')
        else:
            print('Hotel inválido.\n')

    def delete_hotel(db):
        system('cls')
        print('Hotéis')
        hotels = Hotel.display_hotels(db)
        choice = input('Qual hotel deseja excluir? ')
        int_choice = int(choice)
        if int_choice in range(1, len(hotels) + 1):
            Database.exclude_hotel(db, choice)
