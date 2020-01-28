import requests

from tg import create_telegram_bot


def check(devman_token, telegram_token, telegram_chatid):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {devman_token}'
    }
    params = {
        'timestamp': ''
    }

    while True:
        try:
            response = requests.get(url, params=params, headers=headers).json()
        except requests.exceptions.ReadTimeout:
            continue
        except requests.ConnectionError:
            continue
        if response['status'] == 'found':
            lesson_chacked = response['new_attempts'][0]
            lesson_name = lesson_chacked['lesson_title']
            lesson_fails = lesson_chacked['is_negative']
            message_for_lesson = f'Преподаватель проверил работу! "{lesson_name}"'
            create_telegram_bot(telegram_token, telegram_chatid, message_for_lesson, lesson_fails)
            continue
        params = {
            'timestamp': response['timestamp_to_request']
        }
