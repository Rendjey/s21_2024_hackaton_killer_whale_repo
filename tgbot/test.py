# Importing required libraries 
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

# Put the token that you received from BotFather in the quotes 
bot = Bot(token='6396741710:AAG8bNPrWBBJWDfl8H7T76_i63IZnx7uYqw') 

# Initializing the dispatcher object 
dp = Dispatcher(bot) 

# Defining and adding buttons 
button1 = InlineKeyboardButton(text="button1", callback_data="In_First_button") 
button2 = InlineKeyboardButton( 
	text="button2", callback_data="In_Second_button") 
keyboard_inline = InlineKeyboardMarkup().add(button1, button2) 

# Message handler for the /button1 command 


@dp.message_handler(commands=['start']) 
async def check(message: types.Message): 
	await message.reply("hi! how are you", reply_markup=keyboard_inline) 

# Callback query handler for the inline keyboard buttons 


@dp.callback_query_handler(text=["In_First_button", "In_Second_button"]) 
async def check_button(call: types.CallbackQuery): 

	# Checking which button is pressed and respond accordingly 
	if call.data == "In_First_button": 
		await call.message.answer("Hi! This is the first inline keyboard button.") 
	if call.data == "In_Second_button": 
		await call.message.answer("Hi! This is the second inline keyboard button.") 
	# Notify the Telegram server that the callback query is answered successfully 
	await call.answer() 

# Start the bot 
executor.start_polling(dp) 
