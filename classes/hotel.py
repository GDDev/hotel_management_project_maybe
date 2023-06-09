from data.database import Database
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
        print('Hotéis')
        hotels = Hotel.display_hotels(db)
        choice = input('Qual hotel deseja alterar? ')
        if int(choice) in range(1, len(hotels) + 1):
            def change_hotel_name():
                pass
            def change_hotel_address():
                pass
            def change_hotel_city():
                pass
            def change_hotel_state():
                pass
            def change_hotel_country():
                pass
        else:
            print('Hotel inválido.\n')
