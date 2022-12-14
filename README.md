# Дерево компаний

## Описание проекта
Проект позволяет создать древовидную структуру компаний с родительскими и дочерними компаниями. В каждой компании могут быть трудоустроены сотрудники. 

## Технологии
- Python
- Django
- Bootstrap
- Django MPTT

## Запуск и настройка проекта
1. Скачать проект из репозитория: https://github.com/RitisBarauskas/tree_enterprises.git
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать виртуальное окружение: `source venv/scripts/activate`
4. Установить зависимости: `pip install -r requirements.txt`
5. Выполнить миграции: `python manage.py migrate`
6. При необходимости создать тестовые организации: `python manage.py generate_enterprises` или `python manage.py generate_enterprises -del` для удаления всех текущих записей.
7. При необходимости создать тестовых сотрудинков: `python manage.py generate_employees` или `python manage.py generate_employees -del` для удаления текущих записей.
8. Создать суперпользователя: `python manage.py createsuperuser`
9. Собрать статику: `python manage.py collectstatic`
10. Запустить проект: `python manage.py runserver`

## Навигация
1. Список организаций: `http://127.0.0.1:8000/`
2. Список сотрудников компании: `http://127.0.0.1:8000/<id компании>/`
3. Детальная информация о сотруднике: `http://127.0.0.1:8000/employee/<id сотрудинка>/`

## Автор
Ритис Бараускас
TG: @developerperm