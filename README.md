# tree_menu

# Описание
Проект tree_menu предназначено для управления и отображения древовидного меню и пунктов меню. Оно позволяет пользователям создавать меню и пункты в этих меню, просматривать их и управлять ими.

## Стек технологий:
- Python 3.7
- Django 4.2.9
- SQLite

## Как запустить проект:
- Клонирование репозитория в командной строке

`git clone https://github.com/cenme37/tree_menu.git`

- Cоздать и активировать виртуальное окружение:

`python -m venv venv`

`. venv/bin/activate`

- Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

- Выполнить миграции:

`python manage.py migrate`

- Запуск сервера:

`python manage.py runserver`

## Импорт данных из CSV в БД
Этот скрипт предназначен для импорта данных из файлов CSV в базу данных. Он использует модуль csv для чтения CSV файлов, записи и удалениия данных в SQLite базе данных.

### Использование
1. Для загрузки данных - запустить скрипт, выполнив команду `python manage.py import_date -a`.
2. Для удаления данных - запустить скрипт, выполнив команду `python manage.py import_date -с`.

### Варианты команд
1. `-a, --all` - импортировать все таблицы из CSV в базу данных.
2. `-c, --clear` - удалить все данные из базы данных. 

### Важно
Убедитесь, что у вас есть соответствующие CSV файлы в директории `api_yamdb/static/data/` перед запуском скрипта.

#### Пример запроса API
Просмотр древовидного меню:  
```bas
GET /tree/
```
### Важно
Убедитесь, что URL модели - меню совпадает с URL `{% draw_menu 'tree' %}` в HTML-шаблоне index.html.

#### Автор
- Александр Кондрашов