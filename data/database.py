import sqlite3, data.connection as connection
from passlib.hash import bcrypt
from utils.custom_exceptions import PermissionError
from utils import setup as stp
from classes.admin import Admin

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
    # Inserindo um usuário ADMIN padrão
    # Definitivamente não precisa remover isso antes da produção :)
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
        return Admin(username, password)

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

    # Criando função para verificar se o usuário é ADMIN
    def login(self, user):
        if user.role == 'admin':
            self.is_admin = True

    # Função para chamar a função que verifica o tipo de usuário... Não me pergunte
    def check_admin_access(self):
        if not self.is_admin:
            raise PermissionError()

    # Função para inserir um novo usuário
    def insert_user(self, username, password, role = 'receptionist'):
        # Checando se o usuário tem permissões para realizar essa inserção
        self.check_admin_access()
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

    # Criando função para listar os quartos
    # def get_all_rooms(self):
    #     rooms = []
    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute('SELECT * FROM Rooms')
    #         rooms = cursor.fetchall()
    #         cursor.close()
    #     except sqlite3.Error as e:
    #         print(e)
    #     finally:
    #         if self.connection:
    #             self.connection.close()
    #     return rooms
