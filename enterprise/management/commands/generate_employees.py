import datetime
import random
from string import ascii_letters

from django.core.management.base import BaseCommand

from enterprise.models import Enterprise, Employee, CardEmployee
from enterprise.enums import RolesEmployeeEnum


class Command(BaseCommand):
    """
    Генератор сотрудников.

    Для запуска необходимо выполнить команду:
        python manage.py generate_employees
    """
    help = 'Генератор сотрудников'

    @staticmethod
    def __generate_data() -> str:
        """
        Генератор случайных имен
        """
        length = random.choice(range(3,12))
        return ''.join(random.choices(list(ascii_letters), k=length)).capitalize()

    def handle(self, *args, **options) -> None:
        Employee.objects.all().delete()
        CardEmployee.objects.all().delete()
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
