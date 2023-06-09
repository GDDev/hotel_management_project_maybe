import sqlite3, data.connection as connection
from passlib.hash import bcrypt
from utils.custom_exceptions import PermissionError
from utils import setup as stp

# Criando o banco de dados
class Database:
    # Definindo os atributos padrão
    def __init__(self, db_name):
        # Definindo o nome do db
        self.db_name = db_name
        # Definindo a conexão como fechada
        self.connection = None
        # Definindo o usuário como padrão
        self.is_admin = False

    # Função para atribuir a conexão ao atributo
    def connect(self):
        self.connection = connection.create_connection(self.db_name)

    # Função para remover a atribuição da conexão
    def disconnect(self):
        connection.kill_connection(self.connection)
        self.connection = None

    # Função para chamar a criação das tabelas
    def create_tables(self):
        connection.create_tables(self.connection)

    # Inserindo um usuário ADMIN inicial
    def insert_admin_user(self):
        # Criando a query de comando
        query = 'INSERT INTO users (username, password, role) VALUES (?, ?, ?)'
        # Definindo as variáveis
        username, password, role = stp.setup_admin_user()
        # Chamando o método de encriptação da senha
        hashed_password = self.hash_password(password)
        # Atribuindo as variáveis aos placeholders da query
        values = (username, hashed_password, role)
        try:
            # Criando o executor de comandos
            cursor = self.connection.cursor()
            # Executando a query
            cursor.execute(query, values)
            # Confirmando as alterações
            self.connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            return username, password

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


    # Criando função para inicializar o banco de dados
    def initialize(self):
        # Criando conexão
        self.connect()
        # Criando as tabelas
        self.create_tables()
        # Chamando função de boas-vindas
        stp.greetings()
        # Criando um usuário padrão
        username, password = self.insert_admin_user()
        # Fechando a conexão
        self.disconnect()
        return (username, password)

    # Criando função para recuperar todos os usuários do db
    def get_all_users(self):
        # Conectando com o db
        self.connect()
        # Criando uma variável para armazenar os usuários
        users = []
        try:
            # Criando o executor
            cursor = self.connection.cursor()
            # Executando a busca pelos usuários
            cursor.execute('SELECT * FROM Users')
            # Armazenando o resultado na variável
            users = cursor.fetchall()
            # Encerrando o executor
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Encerrando a conexão
                self.connection.close()
        return users
    
    def get_hotel(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = 'SELECT * FROM Hotels WHERE id == ?'
            value = str(id)
            cursor.execute(query, value)
            hotel = cursor.fetchall()
            return hotel[0]
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

    # Função para inserir um novo usuário
    def insert_user(self, username, password, role = 'receptionist'):
        try:
            # Criando o executor
            cursor = self.connection.cursor()
            # Criando a query de inserção
            query = 'INSERT INTO users (username, password, role) VALUES (?, ?, ?)'
            # Encriptação da senha
            hashed_password = self.hash_password(password)
            values = (username, hashed_password, role)
            # Execução da query com a substituição dos placeholders
            cursor.execute(query, values)
            # Confirmação das alterações
            self.connection.commit()
            # Encerramento do executor
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Fechando a conexão
                self.connection.close()

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
            # Encerramento do executor
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                # Fechando a conexão
                self.disconnect()
    
    def update_hotel(self, id, *args):
        try:
            name, address, city, state, country = args
            query = 'UPDATE Hotels SET name = ?, address = ?, city = ?, state = ?, country = ?'
            db_id, db_name, db_addr, db_city, db_state, db_ctr = self.get_hotel(id)
            if name != db_name: db_name = name
            if address != db_addr: db_addr =  address
            if city != db_city: db_city = city
            if state != db_state: db_state = state
            if country != db_ctr: db_ctr = country
            values = (db_name, db_addr, db_city, db_state, db_ctr)
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
            pass
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.connection:
                self.disconnect()
                