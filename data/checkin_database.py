import sqlite3
from data.database import Database

class CheckInDatabase(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_checkin(self, checkin):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'INSERT INTO Checkins (check_in, guest_id, room_id, hotel_id) VALUES (?, ?, ?, ?)'
            check_in_date, guest_id, room_id, hotel_id = checkin
            values = (check_in_date, guest_id, room_id, hotel_id)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.execute('SELECT id FROM Checkins ORDER BY id DESC LIMIT 1')
            checkin_id = cursor.fetchone()
            cursor.close()
            return checkin_id
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_all_checkins(self, hotel_id):
        checkins = []
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = ('SELECT * FROM Checkins WHERE hotel_id == ?')
            value = str(hotel_id)
            cursor.execute(query, value)
            checkins = cursor.fetchall()
            cursor.close()
            return checkins
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_guest_history(self, guest_id):
        checkins = []
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Checkins WHERE guest_id == ?'
            value = str(guest_id)
            cursor.execute(query, value)
            checkins = cursor.fetchall()
            cursor.close()
            return checkins
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def check_out(self, checkin_id, checkout_date):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'UPDATE Checkins SET check_out = ? WHERE id == ?'
            values = (checkout_date, checkin_id)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
