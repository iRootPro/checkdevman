import requests


def check(token):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {token}'
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
            return f'Преподаватель проверил работу! "{lesson_name}"', lesson_fails
        params = {
            'timestamp': response['timestamp_to_request']
        }
