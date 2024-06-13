import sqlite3
from global_variables.variable_holder import db_path


def create_db():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "info" (
        "vk_id" INTEGER,
        "Name" TEXT,
        "Achievement1" INTEGER,
        "Achievement2" INTEGER
        )
        ''')
    cursor.close()
    connection.commit()


def new_user(vk_id, user_name):
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sqlite_select_ids = "SELECT vk_id FROM info;"
    cursor.execute(sqlite_select_ids)
    ids = cursor.fetchall()
    if str(vk_id) not in str(ids):
        sqlite_insert_query = "INSERT INTO info('vk_id', 'Name', 'Achievement1', 'Achievement2') values(?, ?, ?, ?);"
        data = (vk_id, user_name, 0, 0)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        return 1
    else:
        return 0
