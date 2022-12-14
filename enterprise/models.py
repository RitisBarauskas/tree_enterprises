from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

from enterprise.enums import RolesEmployeeEnum


class Enterprise(MPTTModel):
    """
    Предприятие.
    """
    name = models.CharField(
        verbose_name='Название организации',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание организации',
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская организация',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи',
        auto_now_add=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique=True,
    )

    class MPTTMeta:
        order_insertion_by = ('id',)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('parent', 'slug'),
                name='slug_parent_constraint',
            ),
        ]
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('enterprises:employees-by-enterprises', args=[self.id])


class Employee(models.Model):
    """
    Сотрудник.
    """
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    family_name = models.CharField(
        verbose_name='Фамилия',
        max_length=255,
    )
    father_name = models.CharField(
        verbose_name='Отчество',
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.family_name} {self.name} {self.father_name}'

    @property
    def full_name(self):
        return f'{self.family_name} {self.name} {self.father_name}'


class CardEmployee(models.Model):
    """
    Карточка сотрудника.
    """
    employee = models.OneToOneField(
        Employee,
        verbose_name='Сотрудник',
        on_delete=models.CASCADE,
        related_name='cards',
    )
    enterprise = models.ForeignKey(
        Enterprise,
        verbose_name='Организация',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='cards',
    )
    role = models.CharField(
        verbose_name='Должность',
        choices=RolesEmployeeEnum.choices(),
        default=RolesEmployeeEnum.DIRECTOR,
        max_length=50,
    )
    salary = models.PositiveIntegerField(
        verbose_name='Заработная плата',
    )
    date_start = models.DateField(
        verbose_name='Дата трудоустройства',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Карточка сотрудника'
        verbose_name_plural = 'Карточки сотрудников'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.employee} ({RolesEmployeeEnum[self.role].value})'

    @property
    def full_name_and_role(self):
        return (
            f'{self.employee.full_name} '
            f'({RolesEmployeeEnum[self.role].value})'
        )

    @property
    def role_view(self):
        return f'{RolesEmployeeEnum[self.role].value}'
