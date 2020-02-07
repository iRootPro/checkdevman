from dotenv import load_dotenv
import os
import logging.config

from settings import logger_config
from check import check


logging.config.dictConfig(logger_config)
devman_logger = logging.getLogger('devman_logger')


def main():
    DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')

    devman_logger.debug('Бот запущен')
    try:
    	check(DEVMAN_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHATID)
    except Exception as error:
    	devman_logger.error(error, exc_info=True)

if __name__ == '__main__':
    load_dotenv()
    main()

