
from handlers.common import router as common_router
from keyboards.inline import some_keyboard

TOKEN = "8190912145:AAF0JZIrSyblCJXtqdJVYEDA_sT0jJI0RIM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Меня зовут Валерия Марченко. Я хореограф.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
