import random
from string import ascii_letters

from django.core.management.base import BaseCommand
from django.db import transaction

from enterprise.models import Enterprise


class Command(BaseCommand):
    """
    Генератор организаций.

    Для запуска необходимо выполнить команду:
        python manage.py generate_enterprises
        python manage.py generate_enterprises -del
    """
    help = 'Генератор организаций'

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
            Enterprise.objects.update(parent=None)
            Enterprise.objects.all().delete()

        with transaction.atomic():
            parent_ent = Enterprise.objects.create(
                name='Head inc',
                description='Самая главная организация',
                parent=None,
                slug='head',
            )
            for i in range(5):
                for level in range(5):
                    last_ent = Enterprise.objects.order_by('id').last()
                    Enterprise.objects.create(
                        name=f'{self.__generate_data()}',
                        description='Дочерняя организация',
                        parent=(last_ent if level else parent_ent),
                        slug=f'slug{level}{i}',
                    )
