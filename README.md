# CT_restaurant

Файл окружения `.env`, а также базу данных `db.sqlite3` (если имеется) необходимо расположить в корне проекта.

- Используйте `Python 3.10`
- Создайте виртуальное окружение или используйте окружение текущего пользователя *(не рекомендуется)*
- Установите все необходимые зависимости командой:
`pip install -r requirements.txt`
- Выполняем стартовые миграции:
`python manage.py migrate`
- *(если база новая)* Создаем пользователя с админскими правами:
`python manage.py createsuperuser`
- Локально запускаем проект:
`python manage.py runserver`
- **Переходим по ссылке:**
http://127.0.0.1:8000/api/v1/foods/

> Проект возвращает список, содержащий категории еды. Также можно запросить еду по конкретной категории, 
> перейдя по ссылке вида: http://127.0.0.1:8000/api/v1/foods/$pk$/

## en
Locate `.env` environment file and `db.sqlite3` database file *(if available)* in the root directory of the project.

- Use `Python 3.10`
- Create virtual environment or use global environment of current user *(not recommended)*
- Install all necessary requirements via command:
`pip install -r requirements.txt`
- Run initial migrations:
`python manage.py migrate`
- *(if DB is new)* Create superuser with admin permissions:
`python manage.py createsuperuser`
- Run project locally via command:
`python manage.py runserver`
- **Go to the URL:**
http://127.0.0.1:8000/api/v1/foods/

> The project returns a list containing categories of food. It is also possible to query food by 
> a specific category following URL like: http://127.0.0.1:8000/api/v1/foods/$pk$/
