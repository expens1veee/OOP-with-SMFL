from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback

green = KeyboardButtonColor.POSITIVE
red = KeyboardButtonColor.NEGATIVE
blue = KeyboardButtonColor.PRIMARY


def admin_kb() -> Keyboard:
    return (
        Keyboard()
        .add(Text("Сделать рассылку"), color=blue)
        .row()
        .add(Text("Рассылка 1 ачивки"), color=blue)
        .row()
        .add(Text("Рассылка 2 ачивки"), color=blue)
        .row()
        .add(Text("Выход"), color=red)
    )


def accept_spam_kb() -> Keyboard:
    return (
        Keyboard(inline=True)
        .add(Callback(label='Подтвердить', payload={'cmd': 'accept'}))
        .add(Callback(label='Отменить', payload={'cmd': 'cancel'}))
    )
