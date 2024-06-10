from apscheduler.schedulers.asyncio import AsyncIOScheduler
from vkbottle import BuiltinStateDispenser, CtxStorage, KeyboardButtonColor
from vkbottle.framework.labeler import BotLabeler

state_dispenser = BuiltinStateDispenser()
deadline_scheduler = AsyncIOScheduler()
labeler = BotLabeler()
ctx = CtxStorage()

user_accounting = set()

admin_id = [270739574, 546117535]  # id админов

green = KeyboardButtonColor.POSITIVE
red = KeyboardButtonColor.NEGATIVE
blue = KeyboardButtonColor.PRIMARY

db_path = r"database/database.db"
