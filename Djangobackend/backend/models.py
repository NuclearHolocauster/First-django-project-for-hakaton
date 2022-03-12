from django.db import models


class User(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=128)
    CATEGORY_TYPES = (
        (1, 'Студент'),
        (2, 'Преподаватель'),
        (3, 'Сотрудник')
    )
    category = models.IntegerField(verbose_name='Категория', choices=CATEGORY_TYPES)
    login = models.CharField(verbose_name='Логин', max_length=64)
    password = models.CharField(verbose_name='Пароль', max_length=64, editable=False)

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


class Room(models.Model):
    audience_number = models.CharField(primary_key=True, verbose_name='Номер аудитории', unique=True, max_length=64)
    description = models.CharField(verbose_name='Описание', max_length=128)
    capacity = models.CharField(verbose_name='вместимость(чел)', max_length=64)
    Photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.audience_number

    class Meta:
        verbose_name = 'Аудитории'
        verbose_name_plural = 'Аудитории'


class Equipment(models.Model):
    audience_number = models.ForeignKey(Room, verbose_name='Номер аудитории', on_delete=models.CASCADE)
    equipment_name = models.CharField(verbose_name='Наименование оборудования', max_length=64)
    number = models.PositiveIntegerField(verbose_name='Кол-во оборудования в аудитории')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class Reservation(models.Model):
    user = models.ForeignKey(User, verbose_name='Кто забронировал', on_delete=models.CASCADE)
    event = models.CharField(verbose_name='Для чего бронь', max_length=128)
    audience_number = models.ForeignKey(Room, verbose_name='Номер аудитории', on_delete=models.CASCADE)
    reservation_start = models.DateTimeField(verbose_name='Дата и время начала брони',  null=True, blank=True, unique=True)
    reservation_end = models.DateTimeField(verbose_name='Дата и время окончания брони', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
