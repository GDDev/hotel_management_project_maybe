import sqlite3
from data.database import Database

class GuestDatabase(Database):
    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_guest(self, guest):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'INSERT INTO Guests (name, last_name, email, phone) VALUES (?, ?, ?, ?)'
            name, last_name, email, phone = guest
            values = (name, last_name, email, phone)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.execute('SELECT id FROM Guests ORDER BY id DESC LIMIT 1')
            guest_id = cursor.fetchone()[0]
            cursor.close()
            return guest_id
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_guest_by_name(self, guest_name):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Guests WHERE name == ?'
            value = (guest_name.upper(),)
            cursor.execute(query, value)
            guest = cursor.fetchall()
            cursor.close()
            return guest
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_all_guests(self):
        guests = []
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Guests')
            guests = cursor.fetchall()
            cursor.close()
            return guests
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
    