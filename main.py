from dotenv import load_dotenv
import os

from check import check
from tg import  create_telegram_bot


def main():
    DEVMAN_TOKEN = os.getenv('DEVMAN_TOKEN')
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHATID = os.getenv('TELEGRAM_TOKEN')

    message_for_lesson, lesson_fails = check(DEVMAN_TOKEN)
    create_telegram_bot(TELEGRAM_TOKEN, TELEGRAM_CHATID, message_for_lesson, lesson_fails)

if __name__ == '__main__':
    load_dotenv()
    main()
