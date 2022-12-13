from django.db import models

from enterprise.enums import RolesEmployeeEnum


class Enterprise(models.Model):
    """
    Предприятие
    """
    name = models.CharField(
        verbose_name='Название организации',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание организации',
    )
    parent = models.ForeignKey(
        'Enterprise',
        verbose_name='ID родительского предприятия',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='enterprises',
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Сотрудник
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


class CardEmployee(models.Model):
    """
    Карточка сотрудника
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