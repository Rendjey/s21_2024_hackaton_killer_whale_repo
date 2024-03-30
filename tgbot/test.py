import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать, введите свой никнейм на платформе")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = 'http://83.147.246.223:6000/'  # Замените URL на нужный
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Успех: {response.json()}')
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response.status_code)
    except Exception as err:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{err}\n\nСвязь с сервером потеряна')


if __name__ == '__main__':
    application = ApplicationBuilder().token('6611074263:AAEiT9jX3C7hnMc8toJ54Yc3DsY1qjsPfcA').build()
    
    start_handler = CommandHandler('start', start)
    start_ping = CommandHandler('ping', ping)
    application.add_handler(start_handler)
    application.add_handler(start_ping)
    
    application.run_polling()