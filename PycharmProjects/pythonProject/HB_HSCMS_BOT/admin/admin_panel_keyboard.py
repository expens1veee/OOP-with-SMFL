from vkbottle import Keyboard, KeyboardButtonColor, Text

green = KeyboardButtonColor.POSITIVE
red = KeyboardButtonColor.NEGATIVE
blue = KeyboardButtonColor.PRIMARY


def admin_keyboard() -> Keyboard:
    return (
    Keyboard()
        .add(Text("Изменить команды"), color=green)
        .row()
        .add(Text("Сделать рассылку"), color=blue)
        .row()
        .add(Text("Перезагрузить бота"), color=red)
        .row()
        .add(Text("Выход"), color=red)
    )


def teams_keyboard() -> Keyboard:
    kb = Keyboard()
    pass
