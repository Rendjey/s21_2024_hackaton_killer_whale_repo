import config
import backendConect
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    error, message = backend.login(update.effective_chat.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )

if __name__ == '__main__':
    appConfig = config.Config("bot.config")
    backend = backendConect.backConect(appConfig.backendApi)

    application = ApplicationBuilder().token(appConfig.get_tokenTG()).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()