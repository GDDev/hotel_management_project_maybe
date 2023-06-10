from datetime import datetime

class Checkin:
    def __init__(self, checkin_id, checkin_date, guest_id, room_id, hotel_id):
        self.checkin_id = checkin_id
        self.checkin_date = checkin_date
        self.checkout_date = None
        self.guest_id = guest_id
        self.room_id = room_id
        self.hotel_id = hotel_id

    def check_in():
        return datetime.now()

    def check_out(self):
        self.checkout_date = datetime.now()
        nights = self.checkin_date.timestamp() - self.checkout_date.timestamp()
        print(nights)
