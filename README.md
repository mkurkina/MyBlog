# MyBlog

Учебный проект на Django — блог о дизайне, технологиях и цифровом творчестве.

## Функциональность

- Главная страница со списком публикаций.
- Страница «О блоге».
- Страница отдельной публикации.
- Наследование HTML-шаблонов.
- Подключение CSS-стилей и изображений.
- Адаптивное оформление сайта.

## Установка и запуск

Для запуска проекта необходим Python 3.13.

1. Клонировать репозиторий:

```bash
git clone https://github.com/mkurkina/MyBlog.git
cd MyBlog
```

2. Создать виртуальное окружение:

```bash
python3 -m venv .venv
```

3. Активировать виртуальное окружение (macOS/Linux):

```bash
source .venv/bin/activate
```

Для Windows:

```bash
.venv\Scripts\activate
```

4. Установить зависимости:

```bash
python -m pip install -r requirements.txt
```

5. Выполнить миграции:

```bash
python manage.py migrate
```

6. Запустить сервер:

```bash
python manage.py runserver
```

7. Открыть в браузере:

http://127.0.0.1:8000/

## Используемые технологии

- Python
- Django
- HTML
- CSS
- Git и GitHub