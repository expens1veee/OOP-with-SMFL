from vkbottle.bot import Message, BotLabeler
from vkbottle import GroupTypes, GroupEventType, ShowSnackbarEvent
from global_variables.states import BotStates
from global_variables.variable_holder import admin_id
from global_variables.token import api
from global_variables.variable_holder import state_dispenser, ctx
from user.user_keyboards import main_kb, complete_kb, back_kb
from admin.admin_panel_keyboard import admin_kb, accept_spam_kb


admin_labeler = BotLabeler()
admin_labeler.vbml_ignore_case = True


@admin_labeler.private_message(text="Админ-панель")
async def admin_panel(message: Message):
    if message.from_id not in admin_id:
        await message.answer("Тебе сюда нельзя!")
    else:
        await message.answer("Admin panel works!", keyboard=admin_kb())


@admin_labeler.private_message(text="Сделать рассылку")
async def admin_call_post(message: Message):
    await message.answer('Напиши текст, для рассылки', keyboard=back_kb())
    await state_dispenser.set(message.from_id, BotStates.INPUT_SPAM)


@admin_labeler.private_message(state=BotStates.INPUT_SPAM)
async def input_spam(message: Message):
    ctx.set('admin_spam_text', message.text)
    await message.answer(f'Текст для отправки:\n\n{message.text}', keyboard=accept_spam_kb())


@admin_labeler.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def call_back_spam(event: GroupTypes.MessageEvent):
    decision = event.object.payload.get('cmd')
    if decision == 'accept':
        conversations = await api.messages.get_conversations(count=200)
        for i in range(conversations.count):
            if conversations.items[i].conversation.peer.type.value == 'user':
                await api.messages.send(peer_id=conversations.items[i].conversation.peer.id,
                                        random_id=0, message=ctx.get('admin_spam_text'))
        await api.messages.send_message_event_answer(
            event_id=event.object.event_id,
            user_id=event.object.user_id,
            peer_id=event.object.peer_id,
            event_data=ShowSnackbarEvent(text="Рассылка была успешно завершена✅"),
        )
        await api.messages.send(
            user_id=event.object.user_id,
            random_id=0,
            peer_id=event.object.peer_id,
            keyboard=admin_kb(),
            message='Менюфка')
    else:
        await api.messages.send(
                        user_id=event.object.user_id,
                        random_id=0,
                        peer_id=event.object.peer_id,
                        keyboard=admin_kb(),
                        message='Менюфка')
    ctx.delete('admin_spam_text')
    await state_dispenser.delete(event.object.user_id)


@admin_labeler.private_message(text="Рассылка 1 ачивки")
async def admin_call_first_achieve(message: Message):
    ctx.set('achievement1', 1)
    conversations = await api.messages.get_conversations(count=200)
    for i in range(conversations.count):
        if conversations.items[i].conversation.peer.type.value == 'user':
            await api.messages.send(peer_id=conversations.items[i].conversation.peer.id,
                                    random_id=0, attachment='photo-213380769_457239544', keyboard=complete_kb())


@admin_labeler.private_message(text="Рассылка 2 ачивки")
async def admin_call_second_achieve(message: Message):
    ctx.set('achievement2', 1)
    conversations = await api.messages.get_conversations(count=200)
    for i in range(conversations.count):
        if conversations.items[i].conversation.peer.type.value == 'user':
            await api.messages.send(peer_id=conversations.items[i].conversation.peer.id,
                                    random_id=0, attachment='photo-213380769_457239545',
                                    message='Для выполнения этой ачивки впиши кодовое слово, полученное от организатора')


@admin_labeler.private_message(text="Выход")
async def admin_back_to_menu(message: Message):
    await message.answer('Выбери интересующую тебя информацию', keyboard=main_kb(message.from_id))
