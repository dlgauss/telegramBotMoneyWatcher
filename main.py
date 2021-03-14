import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from budget_logic import parseText
from budget_logic import get_current_balance

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler(commands=['statistics'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/statistics` command
#     """
#     button_hi = KeyboardButton('Привет! 👋')
#     greet_kb = ReplyKeyboardMarkup()
#     greet_kb.add(button_hi)
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['currentbalance'])
async def current_balance(message: types.Message):
    """
    This handler will be called when user sends `/currentbalance`
    """

    my_balance = get_current_balance()
    for i in my_balance:
        await message.answer(f'{i["name"]}: {i["sum"]}')


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    s = parseText(message.text)

    await message.answer(s)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)