from global_variables.variable_holder import state_dispenser, labeler, ctx
from global_variables.token import api
from user.main_handlers import main_labeler
from admin.admin_panel import admin_labeler
from database.database import create_db
from loguru import logger
from vkbottle import Bot
import sys


def start_bot():
    logger.remove()
    logger.add(sys.stderr, level="ERROR")

    labeler.load(main_labeler)
    labeler.load(admin_labeler)
    create_db()

    bot = Bot(
        api=api,
        labeler=labeler,
        state_dispenser=state_dispenser
    )

    print("Bot is started!")
    ctx.set('achievement1', 0)
    ctx.set('achievement2', 0)

    bot.run_forever()
