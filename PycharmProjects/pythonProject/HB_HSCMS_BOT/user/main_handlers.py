from vkbottle.bot import Message, BotLabeler
from global_variables.token import api
from global_variables.variable_holder import state_dispenser, ctx
from global_variables.states import BotStates
from global_variables.variable_holder import db_path
from database.database import new_user
from user.user_keyboards import main_kb, menu_kb, back_kb
import random
import sqlite3


main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True


@main_labeler.private_message(text=["Начать", "Start"])
async def start(message: Message):
    user = await api.users.get(message.from_id)
    user_name = user[0].first_name + ' ' + user[0].last_name
    new_user(message.from_id, user_name)
    await message.answer('Здарова, волчара🐺', keyboard=main_kb(message.from_id))


@main_labeler.private_message(text="Информация о событии")
async def info(message: Message):
    await message.answer('День рождения ВШКМиС — это мероприятие для студентов нашей высшей школы,'
                         ' где вы сможете погрузиться в невероятную атмосферу ностальгии,'
                         ' а может и узнать для себя что-то новое о прошлом любимой Высшей школы.')


@main_labeler.private_message(text="Меню бара")
async def menu(message: Message):
    await message.answer(
        "Выбери, хочешь ли ты посмотреть всё меню,"
        " или хочешь испытать свою удачу и попробовать случайный коктейль из бара",
        keyboard=menu_kb())


@main_labeler.private_message(text="Случайный коктейль")
async def get_random_cocktail(message: Message):
    cocktails = ["52", "1 литр бензина и 7 щеток", "Страйк", "Диффуры", "Мататумба", "Кибербуллинг", "Сквер","Не баг, а фича","Скорая помощь"]
    await message.answer(
        f'И тебе выпадает Коктейль "{cocktails[random.randint(0, 8)]}", скорее беги и пробуй его на баре!')

@main_labeler.private_message(text="Всё меню")
async def bar_menu(message: Message):
    await message.answer("Лови! Только много не пей)",
                         attachment='photo-213380769_457239546')


@main_labeler.private_message(text="Назад")
async def back_to_menu(message: Message):
    try:
        await state_dispenser.delete(message.from_id)
    except KeyError:
        pass
    await message.answer('Выбери интересующую тебя информацию', keyboard=main_kb(message.from_id))


@main_labeler.private_message(text="Ачивки")
async def achievement(message: Message):
    if ctx.get('achievement1') and ctx.get('achievement2'):
        await message.answer("Ачивки, которые можно заработать",
                             attachment=['photo-213380769_457239544', 'photo-213380769_457239545'])
    elif ctx.get('achievement1') and not ctx.get('achievement2'):
        await message.answer("Ачивки, которые можно заработать",
                             attachment='photo-213380769_457239544')
    elif ctx.get('achievement2') and not ctx.get('achievement1'):
        await message.answer("Ачивки, которые можно заработать",
                             attachment='photo-213380769_457239545')

    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"SELECT Achievement1, Achievement2 FROM info where vk_id =\"{message.from_id}\""
    cursor.execute(sqlite_select_query)
    data = cursor.fetchall()

    achievement_status1 = 'Выполнена!' if data[0][0] else 'Не выполнена'
    achievement_status2 = 'Выполнена!' if data[0][1] else 'Не выполнена'

    await message.answer(f'Твои ачивки:\n\nАчивка 1: {achievement_status1}\n\nАчивка 2: {achievement_status2}')


@main_labeler.private_message(text='Выполнить✅')
async def complete_achievement(message: Message):
    await message.answer('Напиши правильный ответ', keyboard=back_kb())
    await state_dispenser.set(message.from_id, BotStates.CHECK_ANSWER)


@main_labeler.private_message(state=BotStates.CHECK_ANSWER)
async def check_answer_first_achievement(message: Message):
    answer = 'ответ'
    user_answer = message.text
    if user_answer.lower() == answer.lower():

        sqlite_connection = sqlite3.connect(db_path)
        cursor = sqlite_connection.cursor()
        sqlite_update_query = f"UPDATE info SET Achievement1={1} WHERE vk_id={message.from_id}"
        cursor.execute(sqlite_update_query)
        sqlite_connection.commit()

        await message.answer('Поздравляю, ачивка выполнена, жди следующей!', main_kb(message.from_id))
        await state_dispenser.delete(message.from_id)
    else:
        await message.answer('Боюсь, что это неправильный ответ, попробуй еще раз', main_kb(message.from_id))


@main_labeler.private_message(text='Кодовое слово')
async def check_answer_first_achievement(message: Message):
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sqlite_update_query = f"UPDATE info SET Achievement2={1} WHERE vk_id={message.from_id}"
    cursor.execute(sqlite_update_query)
    sqlite_connection.commit()
    await message.answer('Поздравляю, ачивка выполнена!', main_kb(message.from_id))


@main_labeler.private_message(text="Посмотреть разбивки")
async def teams(message: Message):
    photos = [f'photo-213380769_4572395{str(46 + i)}' for i in range(1, 6)]
    await message.answer('Вот все разбивки', attachment=photos)
