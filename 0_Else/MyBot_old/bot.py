import logging
from typing import Text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='Mybot/MyBot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def greet_user(update, context):
    update.message.reply_text('Привет, чувак!')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)
    logging.info(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот запущен') #посмотреть в документах, как добавить инфомрацию про дату и время 
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()