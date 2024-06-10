from HB_HSCMS_BOT.global_variables.variable_holder import db_path
import sqlite3
from HB_HSCMS_BOT.global_variables.token import api

#функция для вызова разбивки всем пользовательям в дб
async def call():
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sqlite_select_ids = "SELECT vk_id FROM info;"
    cursor.execute(sqlite_select_ids)
    ids = cursor.fetchall()
    lst = '' #сюда что-то на подобии разбивки(или список или что-то другое)
    for i in ids:
        await api.messages.send(user_id=i,message=lst)