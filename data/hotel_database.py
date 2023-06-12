import sqlite3
from data.database import Database

class HotelDatabase(Database):

    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_hotel(self, hotel):
        try:
            # Conectando com o db
            self.connect()
            # Criando o executor
            cursor = self.connection.cursor()
            # Criando a query de inserção
            query = 'INSERT INTO Hotels (name, address, city, state, country) VALUES (?, ?, ?, ?, ?)'
            name, address, city, state, country = hotel
            values = (name, address, city, state, country)
            # Execução da query com a substituição dos placeholders
            cursor.execute(query, values)
            # Confirmação das alterações
            self.connection.commit()
            cursor.execute('SELECT id FROM Hotels ORDER BY id DESC LIMIT 1')
            hotel_id = cursor.fetchone()[0]
            cursor.close()
            return hotel_id
            # Encerramento do executor
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Fechando a conexão
                self.disconnect()

    def get_hotel(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Hotels WHERE id == ?'
            value = str(id)
            cursor.execute(query, value)
            hotel = cursor.fetchone()
            cursor.close()
            return hotel
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def get_all_hotels(self):
        hotels = []
        try:
            # Conectando com o db
            self.connect()
            # Criando o executor
            cursor = self.connection.cursor()
            # Executando a busca pelos hotéis
            cursor.execute('SELECT * FROM Hotels')
            # Armazenando o resultado na variável
            hotels = cursor.fetchall()
            # Encerrando o executor
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Fechando a conexão
                self.disconnect()
        return hotels
    
    def get_hotel_by_id(self, hotel_id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Hotels WHERE id == ?'
            value = str(hotel_id)
            cursor.execute(query, value)
            hotel = cursor.fetchone()
            cursor.close()
            return hotel
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
    
    def update_hotel(self, hotel):
        try:
            query = 'UPDATE Hotels SET name = ?, address = ?, city = ?, state = ?, country = ? WHERE id == ?'
            _, db_name, db_addr, db_city, db_state, db_ctr = self.get_hotel(hotel.hotel_id)
            if hotel.name != db_name: db_name = hotel.name
            if hotel.address != db_addr: db_addr =  hotel.address
            if hotel.city != db_city: db_city = hotel.city
            if hotel.state != db_state: db_state = hotel.state
            if hotel.country != db_ctr: db_ctr = hotel.country
            values = (db_name, db_addr, db_city, db_state, db_ctr, hotel.hotel_id)
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

    def exclude_hotel(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = ('DELETE FROM Hotels WHERE id == ?')
            value = id
            cursor.execute(query, value)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()