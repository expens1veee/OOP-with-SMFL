# from vkbottle.bot import Message, BotLabeler
# from HB_HSCMS_BOT.global_variables.variable_holder import admin_id
# from HB_HSCMS_BOT.keyboards.common_keyboards import *
#
#
# admin_labeler = BotLabeler()
# admin_labeler.vbml_ignore_case = True
#
# flag = False
#
# @admin_labeler.private_message(text="admin_panel")
# async def admin_panel(message: Message):
#     if message.from_id not in admin_id:
#         await message.answer("Куда лезем?")
#     else:
#         flag = True
#         await message.answer("Admin panel works!",keyboard=admin_kbrd())