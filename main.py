import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from budget_logic import parseText
from budget_logic import get_current_balance



load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['help'])
async def current_balance(message: types.Message):
    """
    This handler will be called when user sends `/help`
    """
    if message["from"]["id"] == 479032218:
        resp = f'''refill card operation: [ + ]  [ sum ]  [ destination ]   [ source ]
    outcame operation: [ - ] [ sum ]  [ category ]  [ money_source ]
    salary: [ salary ]  [ sum ]  [ money_destination ] 
    '''
    else:
        await message.answer("Access denied")
    await message.answer(resp)


@dp.message_handler(commands=['currentbalance'])
async def current_balance(message: types.Message):
    """
    This handler will be called when user sends `/currentbalance`
    """
    if message["from"]["id"] == 479032218:
        my_balance = get_current_balance()
        for i in my_balance:
            await message.answer(f'{i["name"]}: {i["sum"]}')
    else:
        await message.answer("Access denied")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    if message["from"]["id"] == 479032218:
        s = parseText(message.text)

        print(message)
        await message.answer(s)
    else:
        await message.answer("Access denied")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)