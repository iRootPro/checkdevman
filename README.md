# Check from DevMan

Данный скрипт присылает сообщение в Telegram о статусе проверки домашнего задания с сайта [dvmn.org](https://dvmn.org/).

## Как установить

Python3 должен быть уже установлен в системе.  
Используя `pip` или  `pip3`  (если есть конфликт с python2) необходимо установить  зависимости:

```shell
pip install -r requirements.txt
```

Рекомендуется использовать виртуальное окружение для изоляции проекта.  
Подробности: [virtualenv/venv](https://docs.python.org/3/library/venv.html).

## Необходимые настройки
Для работы скрипта вам понадобится два токена: для вашего бота в Telegram и для сайта [dvmn.org](https://dvmn.org/).

Для получения Telegram **TOKEN** найдите в Telegram @botfather и создайте новый бот. После того, как бот будет создан, вы получите токен.

Для получения **TOKEN** для сайта dvmn.org перейдите по [ссылке](https://dvmn.org/api/docs/).

Также для работы скрипта необходим  **chat_id** в телеграм, чтобы именно вам бот присылал сообщения о статусе проверки задания.
Для получения chat_id напишите в Telegram боту  @userinfobot.

Создайте в директории, где находятся скрипты файл `.env` и пропишите в него полученные данные в таком виде:

```shell
TELEGRAM_TOKEN=ВАШ_ТОКЕН_TELEGRAM
DEVMAN_TOKEN=ВАШ_ТОКЕН_DEVMAN
TELEGRAM_CHATID=ВАШ_ID_TELEGRAM
```

## Как работать со скриптом
Для запуска скрипта наберите следующую команду:
```shell
python3 main.py
```
Скрипт работает постоянно. При изменении статуса проверки задания бот пришлет сообщение, в котором будет указано, принята ваша работа или нужно доработать.
