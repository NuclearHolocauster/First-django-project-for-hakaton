from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('fio', 'category', 'login')
    list_display_links = ('fio', 'category', 'login')
    search_fields = ('fio', 'login')


class EquipmentInLine(admin.TabularInline):
    model = Equipment


class RoomAdmin(admin.ModelAdmin):
    list_display = ('audience_number', 'description', 'capacity', 'get_photo')
    list_display_links = ('audience_number', 'description', 'capacity')
    search_fields = ('audience_number', 'description', 'capacity')
    fields = ('audience_number', 'description', 'capacity', 'get_photo')
    readonly_fields = ('get_photo',)

    inlines = [
        EquipmentInLine,
    ]

    def get_photo(self, data):
        if data.photo:
            return mark_safe(f"<img src='{data.photo.url}' width=100>")

    get_photo.short_description = "Фото аудитории"


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('audience_number', 'equipment_name', 'number')
    list_display_links = ('audience_number', 'equipment_name', 'number')
    search_fields = ('audience_number', 'equipment_name', 'number')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'audience_number')
    list_display_links = ('user', 'event', 'audience_number')
    search_fields = ('user', 'event', 'audience_number')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'audience')
    list_display_links = ('id', 'user', 'event', 'audience')
    search_fields = ('id', 'user', 'event', 'audience')


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Ticket, TicketAdmin)
