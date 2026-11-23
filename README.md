
# MyBlog

Учебный проект на Django по дисциплине «Технологии создания интернет-приложений».

## Требования

- Python 3.13
- Git (для клонирования репозитория)

## Установка и запуск

1. Клонировать репозиторий:

```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd MyBlog
```

2. Создать виртуальное окружение:

```bash
python3 -m venv .venv
```

3. Активировать виртуальное окружение на macOS/Linux:

```bash
source .venv/bin/activate
```

4. Установить зависимости:

```bash
python -m pip install -r requirements.txt
```

5. Применить миграции:

```bash
python manage.py migrate
```

6. Запустить сервер:

```bash
python manage.py runserver
```

7. Открыть в браузере http://127.0.0.1:8000/

## Технологии

Python, Django, SQLite, Git.
