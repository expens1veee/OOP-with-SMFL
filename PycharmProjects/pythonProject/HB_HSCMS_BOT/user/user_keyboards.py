from vkbottle import Keyboard, KeyboardButtonColor, Text
from global_variables.variable_holder import admin_id

green = KeyboardButtonColor.POSITIVE
red = KeyboardButtonColor.NEGATIVE
blue = KeyboardButtonColor.PRIMARY


def main_kb(vk_id) -> Keyboard:
    kb = Keyboard()
    if int(vk_id) in admin_id:
        kb.add(Text("Админ-панель"), color=red)
        kb.row()
    return (
        kb
        .add(Text("Информация о событии"), color=blue)
        .row()
        .add(Text("Меню бара"), color=blue)
        .row()
        .add(Text("Посмотреть разбивки"), color=blue)
        .row()
        .add(Text("Ачивки"), color=blue)
    )


def menu_kb() -> Keyboard:
    return (
        Keyboard()
        .add(Text("Всё меню"), color=green)
        .row()
        .add(Text("Случайный коктейль"), color=green)
        .row()
        .add(Text("Назад"), color=red)
    )


def complete_kb() -> Keyboard:
    return (
        Keyboard(inline=True)
        .add(Text('Выполнить✅'))
    )


def back_kb() -> Keyboard:
    return (
        Keyboard()
        .add(Text('Назад'), color=red)
    )
