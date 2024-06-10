# from vkbottle.bot import Message, BotLabeler
# from HB_HSCMS_BOT.global_variables.states import BotStates
# from HB_HSCMS_BOT.global_variables.variable_holder import state_dispenser
# from HB_HSCMS_BOT.global_variables.token import api
# from HB_HSCMS_BOT.database.database import new_user
# import sqlite3
#
# main_labeler = BotLabeler()
# main_labeler.vbml_ignore_case = True
#
#
# @main_labeler.private_message(text=["Начать", "Start"])
# async def start(message: Message):
#     """ Добавляем человечка, здороваемся"""
#     user = await api.users.get(message.from_id)  # объект юзера
#     user_name = user[0].first_name + ' ' + user[0].last_name  # имя человека
#     new_user(message.from_id, user_name)  # вношу человека в бд
#     await message.answer('Прив')
