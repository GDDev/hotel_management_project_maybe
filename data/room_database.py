import sqlite3
from data.database import Database

class RoomDatabase(Database):
    
    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_room(self, room):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'INSERT INTO Rooms (number, type, capacity, price, is_occupied, hotel_id) VALUES (?, ?, ?, ?, ?, ?)'
            number, type, capacity, price, is_occupied, hotel_id = room
            values = (number, type.value, capacity, price, is_occupied, hotel_id)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.execute('SELECT id FROM Rooms ORDER BY id DESC LIMIT 1')
            room_id = cursor.fetchone()
            cursor.close()
            return (room_id, number, type, capacity, price, is_occupied, hotel_id)
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_hotel_rooms(self, id):
        rooms = []
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Rooms WHERE hotel_id == ?'
            value = str(id)
            cursor.execute(query, value)
            rooms = cursor.fetchall()
            cursor.close()
            return rooms
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_room_by_id(self, room_id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Rooms WHERE id == ?'
            value = str(room_id)
            cursor.execute(query, value)
            room = cursor.fetchone()
            cursor.close()
            return room
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
    
    def checkin_room(self, room_id):
        try:
            query = 'UPDATE Rooms SET is_occupied = ? WHERE id == ?'
            values = (True, room_id)
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def checkout_room(self, room_id):
        try:
            query = 'UPDATE Rooms SET is_occupied = ? WHERE id == ?'
            values = (False, room_id)
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
    