import sqlite3
from data.database import Database
from passlib.hash import bcrypt

class UserDatabase (Database):

    def __init__(self, db_name):
        super().__init__(db_name)

    # *** FUNÇÕES DE MANIPULAÇÃO DE SENHA ***

    # Criação de um método para encriptar a senha
    @staticmethod
    def hash_password(password):
        # Chamando a função de encriptação do Bcrypt e atribuindo a uma variável
        hashed_password = bcrypt.hash(password)
        # Retornando a senha encriptada
        return hashed_password
    
    # Criando função para comparar a senha fornecida com a do db
    def compare_password(password, stored_password):
        # Usando uma função do Bcrypt para realizar a verificação
        if bcrypt.verify(password, stored_password):
            # Retornando Verdadeiro, caso sejam a mesma
            return True
        # Retornando Falso, caso sejam diferentes
        return False             
        
    # Função para inserir um novo usuário
    def insert_user(self, user):
        try:
            # Conectando com o db
            self.connect()
            name, last_name, email, username, password, role, hotel_id = user
            # Criando o executor
            cursor = self.connection.cursor()
            # Criando a query de inserção
            query = 'INSERT INTO Users (name, last_name, email, username, password, role, hotel_id) VALUES (?, ?, ?, ?, ?, ?, ?)'
            # Encriptação da senha
            hashed_password = self.hash_password(password)
            values = (name, last_name, email, username, hashed_password, role, hotel_id)
            # Execução da query com a substituição dos placeholders
            cursor.execute(query, values)
            # Confirmação das alterações
            self.connection.commit()
            # Encerramento do executor
            cursor.execute('SELECT id FROM Users ORDER BY id DESC LIMIT 1')
            user_id = cursor.fetchone()[0]
            cursor.close()
            return user_id
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Fechando a conexão
                self.connection.close()

    # Criando função para recuperar todos os usuários do db
    def get_hotel_staff(self, hotel_id):
        # Criando uma variável para armazenar os usuários
        users = []
        try:
            # Conectando com o db
            self.connect()
            # Criando o executor
            cursor = self.connection.cursor()
            # Executando a busca pelos usuários
            query = 'SELECT * FROM Users WHERE hotel_id == ?'
            value = str(hotel_id)
            cursor.execute(query, value)
            # Armazenando o resultado na variável
            users = cursor.fetchall()
            # Encerrando o executor
            cursor.close()
            return users
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Encerrando a conexão
                self.connection.close()

    def get_user_by_id(self, user_id, hotel_id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Users WHERE id == ? AND hotel_id == ?'
            values = (str(user_id), str(hotel_id))
            cursor.execute(query, values)
            user = cursor.fetchone()
            cursor.close()
            return user
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def update_user(self, user, hotel_id):
        try:
            query = 'UPDATE Users SET name = ?, last_name = ?, email = ?, username = ? WHERE id == ?'
            _, db_name, db_last_name, db_email, db_username, *_ = self.get_user_by_id(user.user_id, hotel_id)
            if user.name != db_name: db_name = user.name
            if user.last_name != db_last_name: db_last_name =  user.last_name
            if user.email != db_email: db_email = user.email
            if user.username != db_username: db_username = user.username
            values = (db_name, db_last_name, db_email, db_username, user.user_id)
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

    def change_password(self, user_id, new_password):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'UPDATE Users SET password = ? WHERE id == ?'
            hashed_password = self.hash_password(new_password)
            values = (hashed_password, str(user_id))
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return hashed_password
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()

    def delete_user(self, user_id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'DELETE FROM Users WHERE id == ?'
            value = str(user_id)
            cursor.execute(query, value)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
