import asyncio
import random

from aiogram import executor, Dispatcher, Bot, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.dispatcher.filters import Command
from aiogram import filters
from magic_filter import MagicFilter


API_TOKEN = '6628779707:AAF8k97doXoAROUS-sY_VnkXCG8tOZ3lJvc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет! Касатик)\n")

@dp.message_handler(commands=['button'])
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки"),
            types.KeyboardButton(text="С подливой"),
            types.KeyboardButton(text="С дедом морозом"),
        ],
        [
            types.KeyboardButton(text="ПИИИИИИИВОООООО"),
            types.KeyboardButton(text="BEEEEEEEEEEEEER"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)



@dp.message_handler(Command('random'))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )

@dp.callback_query_handler(MagicFilter.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)