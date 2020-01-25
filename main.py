from dotenv import load_dotenv
import os

from check import check
from tg import  create_telegram_bot


def main():
    TOKEN_DEVMAN = os.getenv('TOKEN_DEVMAN')
    TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')
    CHATID_TELEGRAM = os.getenv('CHATID_TELEGRAM')

    message_for_lesson, lesson_fails = check(TOKEN_DEVMAN)
    create_telegram_bot(TOKEN_TELEGRAM, CHATID_TELEGRAM, message_for_lesson, lesson_fails)

if __name__ == '__main__':
    load_dotenv()
    main()
