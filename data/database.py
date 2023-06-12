from os import remove
import data.connection as connection
from utils import setup as stp

# Criando o banco de dados
class Database:
    # Definindo os atributos padrão
    def __init__(self, db_name):
        # Definindo o nome do db
        self.db_name = db_name
        # Definindo a conexão como fechada
        self.connection = None

    # *** FUNÇÕES DE CONEXÃO ***

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

    # *** FUNÇÃO DE INICIALIZAÇÃO ***

    # Criando função para inicializar o banco de dados
    def initialize(self, function_hotel, function_user):
        try:
            # Criando conexão
            self.connect()
            # Criando as tabelas
            self.create_tables()
            # Chamando função de boas-vindas
            stp.greetings()
            # Criando um usuário padrão
            user = stp.setup_user(function_user, 1)
            stp.continue_setup()
            hotel = stp.setup_hotel(function_hotel)
            stp.finish_setup()
            # Fechando a conexão
            self.disconnect()
            return (user, hotel)
        except Exception as e:
            self.disconnect()
            print(e)
            remove('hotel.db')
                