from datetime import datetime

class Checkin:
    def __init__(self, guest, room, hotel):
        self.checkin_date = datetime.now()
        self.checkout_date = None
        self.guest_id = guest
        self.room_id = room
        self.hotel_id = hotel

    def check_out(self):
        self.checkout_date = datetime.now()
