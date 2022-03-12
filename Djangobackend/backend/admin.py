from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('fio', 'category', 'login')
    list_display_links = ('fio', 'category', 'login')
    search_fields = ('fio', 'login')


class EquipmentInLine(admin.TabularInline):
    model = Equipment


class RoomAdmin(admin.ModelAdmin):
    list_display = ('audience_number', 'description', 'capacity', 'Photo')
    list_display_links = ('audience_number', 'description', 'capacity', 'Photo')
    search_fields = ('audience_number', 'description', 'capacity', 'Photo')

    inlines = [
        EquipmentInLine,
    ]


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('audience_number', 'equipment_name', 'number')
    list_display_links = ('audience_number', 'equipment_name', 'number')
    search_fields = ('audience_number', 'equipment_name', 'number')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'audience_number', 'reservation_start', 'reservation_end')
    list_display_links = ('user', 'event', 'audience_number', 'reservation_start', 'reservation_end')
    search_fields = ('user', 'event', 'audience_number', 'reservation_start', 'reservation_end')


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Reservation, ReservationAdmin)

