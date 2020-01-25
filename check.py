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
            lesson_name = response['new_attempts'][0]['lesson_title']
            lesson_fails = response['new_attempts'][0]['is_negative']
            return f'Преподаватель проверил работу! "{lesson_name}"', lesson_fails
        params = {
            'timestamp': response['timestamp_to_request']
        }

