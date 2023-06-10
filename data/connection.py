import sqlite3

# Criando conexão com o banco de dados
def create_connection(db_name):
    conn = None
    try:
        # Conectando com o db hotel.db
        conn = sqlite3.connect('hotel.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Criando função para encerrar a conexão com o db
def kill_connection(conn):
    if conn:
        # Fechando a conexão
        conn.close()

# Criando as tabelas do db
def create_tables(conn):
    try:
        # Criando o executor de comandos
        cursor = conn.cursor()

        # Criando a tabela do hotel
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Hotels (
                id INTEGER PRIMARY KEY,
                name TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                country TEXT
            )
        ''')

        # Criando a tabela dos quartos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Rooms (
                id INTEGER PRIMARY KEY,
                number INTEGER,
                type TEXT CHECK(type IN ('Solteiro', 'Casal', 'Master')),
                capacity INTEGER,
                price REAL,
                is_occupied BOOLEAN,
                hotel_id INTEGER,
                FOREIGN KEY (hotel_id) REFERENCES Hotel (id)
            )
        ''')

        # Criando a tabela dos funcionários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                role TEXT CHECK(role IN ('admin', 'receptionist')),
                hotel_id INTEGER,
                FOREIGN KEY (hotel_id) REFERENCES Hotels (id)
            )
        ''')


        # Criando a tabela dos clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Guests (
                id INTEGER PRIMARY KEY,
                name TEXT,
                last_name TEXT,
                email TEXT,
                phone TEXT
            )
        ''')

        # Criando a tabela de Check-In
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Checkins (
                id INTEGER PRIMARY KEY,
                check_in DATE,
                check_out DATE,
                guest_id INTEGER,
                room_id INTEGER,
                hotel_id INTEGER,
                FOREIGN KEY (guest_id) REFERENCES Guests (id),
                FOREIGN KEY (room_id) REFERENCES Rooms (id),
                FOREIGN KEY (hotel_id) REFERENCES Hotels (id)
            )
        ''')

        # Realizando as alterações no db 
        conn.commit()
        # Destruindo o executor de comandos
        cursor.close()
    except sqlite3.Error as e:
        print(e)
