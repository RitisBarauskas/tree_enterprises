from django.core.management.base import BaseCommand

from enterprise.models import Enterprise

class Command(BaseCommand):
    """
    Генератор организаций.

    Для запуска необходимо выполнить команду:
        python manage.py generate_enterprises
    """
    help = 'Генератор организаций'

    def handle(self, *args, **options) -> None:
        parent_ent = Enterprise.objects.create(
            name='Head inc',
            description='Самая главная организация',
            parent=None,
        )
        for i in range(5):
            for level in range(5):
                last_ent = Enterprise.objects.last()
                Enterprise.objects.create(
                    name=f'Организация {i+level}',
                    description='Дочерняя организация',
                    parent=(last_ent if level else parent_ent),
                )
