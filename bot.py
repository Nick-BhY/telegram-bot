import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.exceptions import TelegramAPIError

logging.basicConfig(level=logging.INFO)

TOKEN = "8190912145:AAF0JZIrSyblCJXtqdJVYEDA_sT0jJI0RIM"

try:
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    @dp.message(Command("start"))
    async def start(message: Message):
        await message.answer("<b>Привет! Меня зовут Валерия Марченко! Я сделаю тебя красивой!</b>")

    if __name__ == "__main__":
        dp.run_polling(bot)

except TelegramAPIError as e:
    logging.error(f"Telegram API error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
