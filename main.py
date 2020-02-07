from dotenv import load_dotenv
import os
import logging.config

from settings import logger_config
from check import check


devman_logger = logging.getLogger('devman_logger')


def main():
    logging.config.dictConfig(logger_config)
    DEVMAN_TOKE = os.getenv('DEVMAN_TOKEN')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID')

    devman_logger.debug('Бот запущен')
    try:
        check(DEVMAN_TOKEN, TELEGRAM_TOKEN, TELEGRAM_CHATID)
    except Exception:
        devman_logger.exception('Произошла ошибка')


if __name__ == '__main__':
    load_dotenv()
    main()
