from aiogram import Bot, Dispatcher, executor, types
import random
from dotenv import load_dotenv
import os
load_dotenv()


PROXY_URL = "http://proxy.server:3128"
ak = 'TOKEN'
bot = Bot(token=str(os.environ.get(ak)), proxy=PROXY_URL)

dp = Dispatcher(bot)
chat_id = oken = str(os.environ.get('chat_ID'))


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.chat.id)
    await bot.send_message(message.from_user.id, "Привет")


@dp.message_handler(commands=['d4'])
async def on_message(message: types.Message):
    number = random.randint(1, 4)
    await bot.send_message(chat_id, str(number))


@dp.message_handler(commands=['d6'])
async def on_message(message: types.Message):
    number = random.randint(1, 6)
    await bot.send_message(chat_id, str(number))


@dp.message_handler(commands=['d8'])
async def on_message(message: types.Message):
    number = random.randint(1, 8)
    await bot.send_message(chat_id, str(number))


@dp.message_handler(commands=['d10'])
async def on_message(message: types.Message):
    number = random.randint(1, 12)
    await bot.send_message(chat_id, str(number))


@dp.message_handler(commands=['d12'])
async def on_message(message: types.Message):
    number = random.randint(1, 12)
    await bot.send_message(chat_id, str(number))


@dp.message_handler(commands=['d20'])
async def on_message(message: types.Message):
    number = random.randint(1, 20)
    await bot.send_message(chat_id, str(number))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
