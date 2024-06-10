from vkbottle.bot import Message, BotLabeler
from HB_HSCMS_BOT.global_variables.states import BotStates
from vkbottle import PhotoMessageUploader
from HB_HSCMS_BOT.global_variables.variable_holder import state_dispenser
from HB_HSCMS_BOT.admin.admin_panel_keyboard import *
from HB_HSCMS_BOT.global_variables.token import api
from HB_HSCMS_BOT.database.database import new_user
from HB_HSCMS_BOT.global_variables.variable_holder import admin_id
from HB_HSCMS_BOT.global_variables.variable_holder import db_path
import sqlite3



photo_upd = PhotoMessageUploader(api)


admin_labeler = BotLabeler()
admin_labeler.vbml_ignore_case = True


uploader = PhotoMessageUploader(api)



@admin_labeler.private_message(text="panel")
async def admin_panel(message: Message):
    if message.from_id not in admin_id:
        await message.answer("Куда лезем?")
    else:
        await message.answer("Admin panel works!", keyboard=admin_keyboard())


@admin_labeler.private_message(text="Изменить команду")
async def handle_admin_command(message: Message):
    await message.answer("Менюфка:", keyboard=admin_keyboard(message.from_id, message))
    state = await state_dispenser.get(message.peer_id)
    if state:
        await state_dispenser.delete(message.peer_id)




@admin_labeler.private_message(text="Сделать рассылку")
async def admin_call_rasbiyka(message: Message):
    if message.from_id in admin_id:
        sqlite_connection = sqlite3.connect(db_path)
        cursor = sqlite_connection.cursor()
        sqlite_select_ids = "SELECT vk_id FROM info;"
        cursor.execute(sqlite_select_ids)
        ids = cursor.fetchall()
        photo = await photo_upd.upload("Handlers/Меню.png")

        lst = 'ss'  # сюда что-то на подобии разбивки(или список или что-то другое)
        for i in ids:
            await api.messages.send(user_id=i[0],random_id=0,attachment=photo)


