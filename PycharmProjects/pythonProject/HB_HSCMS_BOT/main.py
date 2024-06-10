from global_variables.variable_holder import state_dispenser, labeler
from global_variables.token import api
from database.database import create_db
from HB_HSCMS_BOT.handlers.main_handlers import main_labeler
from HB_HSCMS_BOT.admin.admin_panel import admin_labeler
from loguru import logger
from vkbottle import Bot
import sys


def start_bot():
    # Настройка логов
    logger.remove()
    logger.add(sys.stderr, level="ERROR")

    # Подключение всех перехватчиков
    labeler.load(main_labeler)
    labeler.load(admin_labeler)
    create_db()

    bot = Bot(
        api=api,
        labeler=labeler,
        state_dispenser=state_dispenser
    )

    print("Bot is started!")

    bot.run_forever()
