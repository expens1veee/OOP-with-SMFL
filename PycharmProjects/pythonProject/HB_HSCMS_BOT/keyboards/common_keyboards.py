from vkbottle import Keyboard, KeyboardButtonColor, Text
green = KeyboardButtonColor.POSITIVE
red = KeyboardButtonColor.NEGATIVE
blue = KeyboardButtonColor.PRIMARY


def main_kbrd() -> Keyboard:
    return (
    Keyboard()
    .add(Text("Информация о событии"), color=blue)
    .row()
    .add(Text("Меню бара"), color=blue)
    .row()
    .add(Text("Моя разбивка"), color=blue)
    .row()
    .add(Text("Ачивки"), color=blue)
    )
def menu_kbrd() -> Keyboard:
    return (
    Keyboard()
    .add(Text("Всё меню"), color=green)
    .row()
    .add(Text("Случайный коктейль"), color=green)
    .row()
    .add(Text("Назад"), color=red)
    )

