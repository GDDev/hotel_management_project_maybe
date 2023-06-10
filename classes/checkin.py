from datetime import datetime

class Checkin:
    def __init__(self, guest_id, room_id, hotel_id):
        self.checkin_date = datetime.now()
        self.checkout_date = None
        self.guest_id = guest_id
        self.room_id = room_id
        self.hotel_id = hotel_id

    def check_out(self):
        self.checkout_date = datetime.now()
