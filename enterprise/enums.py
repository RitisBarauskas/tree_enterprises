import enum


class RolesEmployeeEnum(enum.Enum):
    """
    Должности сотрудников
    """
    MANAGER = 'Менеджер'
    DEVELOPER = 'Разработчик'
    DIRECTOR = 'Руководитель'
    ACCOUNTANT = 'Бухгалтер'

    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)
