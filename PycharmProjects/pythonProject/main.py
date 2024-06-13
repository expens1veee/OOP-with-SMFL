# from vkbottle.bot import Bot, Message
# import aiohttp
# import ssl
#
# ssl_context = ssl.create_default_context()
# ssl_context.check_hostname = False
# ssl_context.verify_mode = ssl.CERT_NONE
#
# session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))
#
#
# bot = Bot(token='vk1.a.Oi5M4imZ1fHK6T8nsCa11VtY2xnoO6-GAPifIKfaYEboKrnk4KeUFTAG4eTvSO1z28pe-vodVuGLrUX1Co4P4N6c0qJ36LUuG9sr70nyW7U1YuvocICfNPzpkuFFCXAE1xRjf30fQlir6nuHGckSYZOdMpwAYJQCfxRCUhsP0jhHQw8t73F65ruKPqCO31-jr7htw8gT4LUA7BuCLBd8bg',session=session )
#
# @bot.on.message()
# async def mes_h(message: Message):
#     await message.answer('hellow')
#


# bot.run_forever()
import ssl
import aiohttp
from vkbottle import Bot, API

# Создание SSL контекста с указанием файла сертификатов
ssl_context = ssl.create_default_context(cafile='/Users/vadimkafanov/Downloads/gseccovsslca2018.crtf')

# Настройка aiohttp клиента
session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context))

# Создание API клиента с использованием настроенного aiohttp клиента
api = API(token="vk1.a.Oi5M4imZ1fHK6T8nsCa11VtY2xnoO6-GAPifIKfaYEboKrnk4KeUFTAG4eTvSO1z28pe-vodVuGLrUX1Co4P4N6c0qJ36LUuG9sr70nyW7U1YuvocICfNPzpkuFFCXAE1xRjf30fQlir6nuHGckSYZOdMpwAYJQCfxRCUhsP0jhHQw8t73F65ruKPqCO31-jr7htw8gT4LUA7BuCLBd8bg", session=session)

# Создание бота
bot = Bot(api=api)

@bot.on.message(text="Привет")
async def hello_handler(message):
    await message.answer("Привет!")

bot.run_forever()
