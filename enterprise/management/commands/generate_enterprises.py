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
        parents = []
        for level in range(5):
            enterprises = [
                Enterprise(
                    name=f'Организация {i}, уровень {level}',
                    description=f'Мощное описание {i**2}',
                    parent_id=(parents[i].id if parents else None)
                ) for i in range(5)
            ]
            Enterprise.objects.bulk_create(enterprises)
            parents = Enterprise.objects.all().order_by('-id')[:5]
