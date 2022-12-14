import datetime
import random
from string import ascii_letters

from django.core.management.base import BaseCommand
from django.db import transaction

from enterprise.enums import RolesEmployeeEnum
from enterprise.models import CardEmployee, Employee, Enterprise


class Command(BaseCommand):
    """
    Генератор сотрудников.

    Для запуска необходимо выполнить команду:
        python manage.py generate_employees
        python manage.py generate_employees -del
    """
    help = 'Генератор сотрудников'

    def add_arguments(self, parser):
        parser.add_argument(
            '-del',
            '--delete',
            action='store_true',
            default=False,
            help='Удаление старых записей',
        )

    @staticmethod
    def __generate_data() -> str:
        """
        Генератор случайных имен
        """
        length = random.choice(range(3, 12))
        return ''.join(
            random.choices(list(ascii_letters), k=length)
        ).capitalize()

    def handle(self, *args, **options) -> None:

        if options.get('delete'):
            print('Удаляем')
            Employee.objects.all().delete()
            CardEmployee.objects.all().delete()

        with transaction.atomic():
            employees = [
                Employee(
                    name=self.__generate_data(),
                    family_name=self.__generate_data(),
                    father_name=self.__generate_data(),
                ) for _ in range(5000)
            ]
            Employee.objects.bulk_create(employees)

            enterprises = Enterprise.objects.all()
            employees_create = Employee.objects.all()
            cards = [
                CardEmployee(
                    employee=employee,
                    enterprise=random.choice(enterprises),
                    role=random.choice(RolesEmployeeEnum.choices_role()),
                    salary=random.choice(range(100, 200)),
                    date_start=datetime.date.today(),
                ) for employee in employees_create
            ]

            CardEmployee.objects.bulk_create(cards)
