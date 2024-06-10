import sqlite3
from HB_HSCMS_BOT.global_variables.variable_holder import db_path


def create_db():  # создает дб
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "teams" (
        "Team_name" TEXT
        )
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "info" (
    'vk_id' INTEGER,
    'Name' TEXT,
    "Team_name" TEXT,
    FOREIGN KEY (Team_name) REFERENCES teams (Team_name)
    )
    ''')
    cursor.close()
    connection.commit()


def new_user(vk_id, user_name):  # добавляет нового юзера
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sqlite_select_ids = "SELECT vk_id FROM info;"
    cursor.execute(sqlite_select_ids)
    ids = cursor.fetchall()
    if str(vk_id) not in str(ids):
        sqlite_insert_query = "INSERT INTO info('vk_id', 'Name', 'Team_name') values(?, ?, ?);"
        data = (vk_id, user_name, 'Без команды')
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        return 1
    else:
        return 0
