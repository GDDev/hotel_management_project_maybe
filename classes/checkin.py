from os import system
from globals import db_name
from classes.room import Room
from datetime import datetime
from data.checkin_database import CheckInDatabase
from utils.custom_exceptions import InvalidChoiceError
from utils.menus import checkout_menu, guest_checkin_menu, menu, checkin_menu

DB = CheckInDatabase(db_name)

class CheckIn:
    def __init__(self, checkin_id, checkin_date, guest_id, room_id, hotel_id, checkout_date=None):
        self.checkin_id = checkin_id
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.guest_id = guest_id
        self.room_id = room_id
        self.hotel_id = hotel_id

    def date_to_str(date):
        return date.strftime("%Y-%m-%d %H:%M:%S")
    
    def str_to_date(str):
        return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")
    
    def check_in(current_hotel, *functions):
        from classes.guest import Guest
        while True:
            rooms = Room.get_available_rooms(current_hotel)
            room = menu(checkin_menu, current_hotel, rooms, *functions)
            if room == 'break':
                break
            elif room:
                guest = menu(guest_checkin_menu, Guest.get_guest_by_name, Guest.create_guest)
                if not guest:
                    print('Nenhum hóspede correspondente à pesquisa.')
                    guest = Guest.create_guest()
                # CheckIn.check_in(CheckIn, guest.guest_id, room.room_id, self.hotel_id)
                date = datetime.now()
                checkin = (CheckIn.date_to_str(date), guest.guest_id, room.room_id, current_hotel.hotel_id)
                DB.insert_checkin(checkin)
                room.checkin_room()
                current_hotel.refresh_hotel()
                print('Check-in realizado com sucesso!')
                input('\nPressione ENTER para continuar...')
                system('cls')
                break

    def check_out(current_hotel):
        while True:
            checkins = menu(checkout_menu, current_hotel, CheckIn)
            if checkins == 'break':
                break
            rooms = Room.get_occupied_rooms(current_hotel)
            Room.display_occupied_rooms(rooms)
            if rooms:
                print('\n0. Voltar')
                choice = input('Informe o número do quarto para realizar o check-out: ')
                int_choice = int(choice)
                if int_choice == 0:
                    break
                for room in rooms:
                    if int_choice == room.number:
                        chosen_room = room
                        for checkin in checkins:
                            if checkin.room_id == chosen_room.room_id:
                                debt = chosen_room.checkout_room()
                                date = datetime.now()
                                checkin.checkout_date = date
                                DB.check_out(checkin.checkin_id, CheckIn.date_to_str(date))
                                nights = checkin.checkout_date - checkin.checkin_date
                                debt = CheckIn.calculate_debt(nights.days, debt)
                                current_hotel.refresh_hotel()
                                print(f'Total a cobrar: R$ {debt:.2f}\n')
                                input('\nPressione ENTER para continuar...')
                                system('cls')
                                break
            else:
                print('Nenhum quarto está ocupado no momento.\n')
                input('Pressione ENTER para continuar...')
                system('cls')

    def get_check_ins(hotel_id):
        checkin_list = []
        checkins = DB.get_all_checkins(hotel_id)
        for checkin in checkins:
            checkin_id, checkin_date, checkout_date, guest_id, room_id, hotel = checkin
            checkin_date = CheckIn.str_to_date(checkin_date)
            if checkout_date:
                checkout_date = CheckIn.str_to_date(checkout_date)
            checkin_class = CheckIn(checkin_id, checkin_date, guest_id, room_id, hotel, checkout_date)
            checkin_list.append(checkin_class)
        return checkin_list
    
    def get_open_checkins(current_hotel):
        open_checkins = []
        checkins = CheckIn.get_check_ins(current_hotel.hotel_id)
        for checkin in checkins:
            if checkin.checkout_date == None:
                open_checkins.append(checkin)
        return open_checkins
    
    def get_guest_history(self, guest_id):
        checkin_list = []
        checkins = DB.get_guest_history(guest_id)
        for checkin in checkins:
            checkin_id, checkin_date, checkout_date, guest, room_id, hotel_id = checkin
            checkin_date = self.str_to_date(checkin_date)
            if checkout_date:
                checkout_date = self.str_to_date(checkout_date)
                checkin_class = CheckIn(checkin_id, checkin_date, guest, room_id, hotel_id, checkout_date)
            else:
                checkin_class = CheckIn(checkin_id, checkin_date, guest, room_id, hotel_id)
            checkin_list.append(checkin_class)
        return checkin_list

    def calculate_debt(nights, price):
        return price * nights
