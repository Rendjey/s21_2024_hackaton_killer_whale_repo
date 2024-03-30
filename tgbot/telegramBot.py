import random
import asyncio
import logging
import config
import backendConect
from datetime import datetime, timedelta
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

appConfig = config.Config("bot.config")
backend = backendConect.backConect(appConfig.backendApi)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=appConfig.TGtoken)
# Диспетчер
dp = Dispatcher()

@dp.message(Command("random"))
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

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    await callback.message.edit_text(
        str(random.randint(1, 10)),
        reply_markup=builder.as_markup()
    )

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    error, answer = backend.login(message.chat.id)
    if error == 0:
        builder.add(types.InlineKeyboardButton(
            text="Бронировать переговорку",
            callback_data="reservRoom")
        )
        builder.add(types.InlineKeyboardButton(
            text="Отменить бронирование",
            callback_data="cancelReserv")
        )
    await message.answer(answer, reply_markup=builder.as_markup())

@dp.callback_query(F.data == "start")
async def send_start_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    error, answer = backend.login(callback.message.chat.id)
    if error == 0:
        builder.add(types.InlineKeyboardButton(
            text="Бронировать переговорку",
            callback_data="reservRoom")
        )
        builder.add(types.InlineKeyboardButton(
            text="Отменить бронирование",
            callback_data="cancelReserv")
        )
        builder.add(types.InlineKeyboardButton(
            text="Тест функции",
            callback_data="test")
        )
    await callback.message.edit_text(answer, reply_markup=builder.as_markup())

@dp.callback_query(F.data == "test")
async def test_fun(callback: types.CallbackQuery):
    today = datetime.now().date()
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="В меню",
        callback_data="start")
    )
    for i in range(7):
        date_text = (today + timedelta(days=i)).strftime("%Y-%m-%d")  # Преобразуем дату в строку
        builder.row(types.InlineKeyboardButton(
            text=date_text,
            callback_data=f"day{i}"
        ))
    await callback.message.edit_text(
        "Выберите день бронирования",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "cancelReserv")
async def cancel_Reserv(callback: types.CallbackQuery):

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="В меню",
        callback_data="start")
    )
    await callback.message.edit_text(
        str(random.randint(1, 10)),
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "reservRoom")
async def send_floor(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="В меню",
        callback_data="start")
    )
    builder.add(types.InlineKeyboardButton(
        text="Этаж 17",
        callback_data="floor17")
    )
    builder.add(types.InlineKeyboardButton(
        text="Этаж 18",
        callback_data="floor18")
    )
    builder.add(types.InlineKeyboardButton(
        text="Этаж 20",
        callback_data="floor20")
    )
    await callback.message.edit_text(
        "Выберите этаж для бронирования",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data.in_({"floor17", "floor18", "floor20"}))
async def floor(callback: types.CallbackQuery):
    chosen_floor = int(callback.data[5:])
    error, answer = backend.get_floor(chosen_floor, callback.message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="В меню",
        callback_data="start")
    )
    await callback.message.edit_text(
        f'{answer}',
        reply_markup=builder.as_markup()
    )

@dp.message(F.text)
async def textParser(message: types.Message):
    error, answer = backend.login(message.chat.id)
    if error == 1:
        error, answer = backend.reg(message.text, message.chat.id)
    else:
        answer = "что? начните с начала /start"

    await message.answer(f"{answer}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())