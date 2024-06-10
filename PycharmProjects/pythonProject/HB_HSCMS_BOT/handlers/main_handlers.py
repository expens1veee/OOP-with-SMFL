from vkbottle.bot import Message, BotLabeler
from vkbottle import  PhotoMessageUploader
from HB_HSCMS_BOT.global_variables.token import api
from HB_HSCMS_BOT.database.database import new_user
from HB_HSCMS_BOT.keyboards.common_keyboards import *
import random
main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True
photo_upd = PhotoMessageUploader(api)


@main_labeler.private_message(text=["Начать", "Start"])
async def start(message: Message):
    """ Добавляем человечка, здороваемся"""
    user = await api.users.get(message.from_id)  # объект юзера
    user_name = user[0].first_name + ' ' + user[0].last_name  # имя человека
    new_user(message.from_id, user_name)  # вношу человека в бд
    await message.answer('Прив',keyboard=main_kbrd())

@main_labeler.private_message(text="Информация о событии")
async def info(message: Message):
    await message.answer('Событие будет тогда-то тогда-то, там-то там-то')

@main_labeler.private_message(text="Меню бара")
async def menu(message: Message):
    await message.answer("Выбери, хочешь ли ты посмотреть всё меню, или хочешь испытать свою удачу и попробовать случайный коктейль из бара", keyboard=menu_kbrd())

@main_labeler.private_message(text="случайный коктейль")
async def randcock(message: Message):
    cocktails = ['52', "1 литр бензина и 7 щеток", "Страйк", "Кчау", "Финазес", "Кибербуллинг"]
    await message.answer(f'И тебе выпадает Коктейль "{cocktails[random.randint(0,5)]}", скорее беги и пробуй его на баре!')

@main_labeler.private_message(text="Всё меню")
async def barmenu(message: Message):
    photo = await photo_upd.upload("Handlers/Меню.png")
    await message.answer("Лови! Только много не пей)",
                         attachment=photo)
    #!!!НЕ ЗАБЫТЬ ПОМЕНЯТЬ ФОТО НА ФОТО МЕНЮ КОГДА ФЕДЯ СКИНЕТ


@main_labeler.private_message(text="Назад")
async def nazad(message: Message):
    await message.answer('Выбери интересующую тебя информацию', keyboard=main_kbrd())




