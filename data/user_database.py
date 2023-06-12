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
