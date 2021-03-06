import requests
import time

from tg import send_tg_message


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
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.ReadTimeout:
            continue
        except requests.ConnectionError:
            time.sleep(120)
            continue
        if response['status'] == 'found':
            lesson_info = response['new_attempts'][0]
            lesson_name = lesson_info['lesson_title']
            lesson_fails = lesson_info['is_negative']
            message_for_lesson = f'Преподаватель проверил работу! "{lesson_name}"'
            send_tg_message(telegram_token, telegram_chatid,
                                message_for_lesson, lesson_fails)
            params = {
                'timestamp': response['last_attempt_timestamp']
            }
            continue
        params = {
            'timestamp': response['timestamp_to_request']
        }
