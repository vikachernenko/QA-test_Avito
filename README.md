# Тестовое задание на стажировку QA в Авито (осень 2025)

Решение двух заданий в одном репозитории:

- Task1 — поиск багов на UI-странице
- Task2 — автотесты API микросервиса объявлений https://qa-internship.avito.com

```plaintext
.
├── Task1
│   ├── screenshot.png
│   └── BUGS_FROM_SCREENSHOT.md
│
├── Task2
│   ├── TESTCASES.md
│   ├── test_api.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

## Описание Task2

Этот проект содержит автоматизированные тесты для микросервиса объявлений Avito QA Internship.  
Тесты полностью соответствуют реальным ручным действиям, выполненным в Postman.

Включены 4 успешных теста:

1. Создание объявления
2. Получение объявления по ID
3. Получение всех объявлений по sellerID
4. Получение статистики по itemID

Негативные тесты не включены.

## Требования

- Python 3.9+
- pip
- pytest
- requests

## Запуск автотестов API (Task2)

1. Клонируйте репозиторий: `git clone https://github.com/vikachernenko/QA-test_Avito.git`
2. Перейдите в рабочую директорию проекта: `cd Task2`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте его:

- Windows: `.\venv\Scripts\activate`
- Linux/MacOS: `source venv/bin/activate`

5. Установите зависимости: `pip install -r requirements.txt`
6. Запустите автотесты: `pytest test_api.py -v`
