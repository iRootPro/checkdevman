import telegram


def create_telegram_bot(token_telegram, message_for_lesson, lesson_fails):
    if lesson_fails:
        message = f'{message_for_lesson}. К сожалению в работе нашли ошибки.'
    else:
        message =  f'{message_for_lesson}. Преподаватель принял работу.'
    bot = telegram.Bot(token=token_telegram)

    bot.send_message(chat_id=34979247, text=message)
