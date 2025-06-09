from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

bot = Bot(token="8190912145:AAF0JZIrSyblCJXtqdJVYEDA_sT0jJI0RIM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Меня зовут Валерия Марченко. Я сделаю тебя красивой")

if __name__ == '__main__':
    executor.start_polling(dp)
