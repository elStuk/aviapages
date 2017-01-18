# Тестовое задание для aviapages.com

Это проект Django, который позволяет пройти процесс аутенфикации через facebook.

Ваша задача состоит в том, чтобы добавить в существующий проект следующий функционал:

* Создать модель Post для записей пользователя.
* На страницу профиля (/profile) добавить форму для Создания записей.
* На главной странице (/) добавить список всех записей от всех пользователей в хронологическом порядке
* При клике на заголовок записи - должна открываться страница этой записи.

Успехов!


## Установка проекта

* Клонировать проект 
* Установить python3
* Установить pip
* Установить virtualenv / virtualenvwrapper

```
cd aptestproject/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
* Перейти в браузере по адресу localhost:8000
