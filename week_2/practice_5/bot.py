import logging
from typing import Text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import settings

logging.basicConfig(filename='MyBot.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def greet_user(update, context):
    update.message.reply_text('Привет, чувак!')

def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)
    logging.info(text)

def planet_detection(update, context):
    today = ephem.now()
    try: 
        planet_name = update.message.text.split()[1].capitalize()
        selected_planet = getattr(ephem, planet_name)
        planet_constellation = ephem.constellation(selected_planet(today))
        update.message.reply_text((f'Планета {planet_name} находится в созвездии: {planet_constellation}'))
        logging.info(planet_name)
    except AttributeError:
        update.message.reply_text('Введите корректное название планеты /planet Name')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_detection))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    logging.info('Бот запущен')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()