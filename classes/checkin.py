from globals import db_name
from datetime import datetime
from data.checkin_database import CheckInDatabase

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

    def get_check_ins(self, hotel_id):
        checkin_list = []
        checkins = DB.get_all_checkins(hotel_id)
        for checkin in checkins:
            checkin_id, checkin_date, checkout_date, guest_id, room_id, hotel = checkin
            checkin_date = self.str_to_date(checkin_date)
            if checkout_date:
                checkout_date = self.str_to_date(checkout_date)
            checkin_class = CheckIn(checkin_id, checkin_date, guest_id, room_id, hotel, checkout_date)
            checkin_list.append(checkin_class)
        return checkin_list
    
    def get_open_checkins(self, hotel_id):
        open_checkins = []
        checkins = self.get_check_ins(self, hotel_id)
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
            checkin_class = CheckIn(checkin_id, checkin_date, guest, room_id, hotel_id)
            checkin_list.append(checkin_class)
        return checkin_list

    def check_in(self, guest_id, room_id, hotel_id):
        date = datetime.now()
        checkin = (self.date_to_str(date), guest_id, room_id, hotel_id)
        checkin_id = DB.insert_checkin(checkin)
        check_in = CheckIn(checkin_id, date, guest_id, room_id, hotel_id)
        return check_in

    def check_out(self):
        date = datetime.now()
        self.checkout_date = date
        DB.check_out(self.checkin_id, CheckIn.date_to_str(date))
        nights = self.checkout_date - self.checkin_date
        return nights.days

    def calculate_debt(nights, price):
        return price * nights
