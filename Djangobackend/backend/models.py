from django.db import models


class User(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=128)
    CATEGORY_TYPES = (
        (1, 'Студент'),
        (2, 'Преподаватель'),
        (3, 'Сотрудник')
    )
    category = models.IntegerField(verbose_name='Категория', choices=CATEGORY_TYPES)


class Room(models.Model):
    audience_number = models.CharField(primary_key=True, verbose_name='Номер аудитории', unique=True, max_length=64)
    description = models.CharField(verbose_name='Описание', max_length=128)
    capacity = models.CharField(verbose_name='вместимость(чел)', max_length=64)


class Equipment(models.Model):
    audience_number = models.ForeignKey(Room, verbose_name='Номер аудитории', on_delete=models.CASCADE)
    equipment_name = models.CharField(verbose_name='Наименование оборудования', max_length=64)
    number = models.IntegerField(verbose_name='Кол-во оборудования в аудитории')


class Reservation(models.Model):
    audience_number = models.ForeignKey(Room, verbose_name='Номер аудитории', on_delete=models.CASCADE)
    reservation_start = models.DateTimeField(verbose_name='Дата и время начала брони',  null=True, blank=True)
    reservation_end = models.DateTimeField(verbose_name='Дата и время окончания брони', null=True, blank=True)
