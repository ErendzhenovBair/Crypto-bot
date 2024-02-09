# Телеграм-бот - Crypto bot

## Описание проекта: Телеграм-бот для отслеживания цен криптовалют

Телеграм бот Crypto Bot является вашим персональным помощником для мониторинга цен на криптовалюты. Этот бот разработан на базе библиотеки aiogram и предоставляет пользователям удобный способ отслеживать текущие цены на различные торговые пары криптовалют на основе ваших данных о количестве токенов.

## Функциональность:

- Выбор торговой пары: Пользователи могут выбирать торговые пары из предоставленного списка.
- Ввод количества токенов: Бот предлагает ввести количество токенов, которое вы хотели бы отслеживать.
- Получение общей стоимости: Бот рассчитывает общую стоимость указанного количества токенов на основе текущей цены каждого токена в паре. Информация запрашивается с биржи Бинанс на текущий момент.
- Отображение результатов: Результаты подсчетов предоставляются в виде ответного сообщения с указанием общей стоимости токенов в USDT (долларах США).

### Технологии

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/-aiogram-464646?style=flat-square&logo=telegram)](https://github.com/aiogram/aiogram)
[![requests](https://img.shields.io/badge/-requests-464646?style=flat-square&logo=requests)](https://github.com/psf/requests)
[![python-binance](https://img.shields.io/badge/-python_binance-464646?style=flat-square&logo=binance)](https://github.com/sammchardy/python-binance)
[![ruff](https://img.shields.io/badge/-ruff-464646?style=flat-square&logo=ruff)](https://github.com/best-doctor/ruff)


- Python 3.10.12
- aiogram 3.3.0
- requests 2.31.0
- python-binance 1.0.19
- ruff 0.2.1

### Запуск проекта локально 

Клонируем себе репозиторий:

```
git clone https://github.com/ErendzhenovBair/.git
```
Cоздаем и активируем виртуальное окружение:

Команда для установки виртуального окружения на Mac или Linux:

```bash
   python3 -m venv venv
   source venv/bin/activate
```

Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

Устанавливаем зависимости из файла requirements.txt:

```bash
   pip install -r requirements.txt
```

- Запустить проет:

```bash
   python app.py
```

- Выбор торговой пары осуществляется в ответ на команду /start в боте

- Количество токенов для расчета возможно представить в виде целого или дробного числа.

### Заполнение env

Для проекта Crypto bot секреты подключаются из файла .env. 
Создайте файл .env и заполните его своими данными. Перечень данных указан в корневой директории проекта в файле .env.example .env.
Проект доступен в телеграме по адресу @cryptoinfodemobot

## Ruff Линтер

Настройки линтера лежат в файле pyproject

Чтобы проверить все файлы в репозитории из корневой дириктории необходимо вызвать

```bash
ruff .
```

Чтобы сразу исправить ошибки импортов необходимо вызвать

```bash
ruff . --fix
```

### Автор проекта

Автор этого проекта - Эрендженов Баир. 
Если у вас есть вопросы, предложения или просто поделитесь своим мнением о проекте, не стесняйтесь обращаться ко мне.
- Электронная почта: erendzhenovbair1990@yandex.ru
- Telegram: @BairErendzhenov
