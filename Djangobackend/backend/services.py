from django_filters import rest_framework as filters
from .models import Equipment, Room


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EquipmentFilter(filters.FilterSet):
    audience_id = CharFilterInFilter(field_name='audience_number', lookup_expr='in')
    equipment_name = CharFilterInFilter(field_name='equipment_name', lookup_expr='in')

    class Meta:
        model = Equipment
        fields = ['audience_number']


class IntFilterInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class RoomCapacityFilter(filters.FilterSet):
    capacity = CharFilterInFilter(field_name='capacity', lookup_expr='in')

    class Meta:
        model = Room
        fields = ['capacity']


class RoomEquipmentFilter(filters.FilterSet):
    equipment_name = CharFilterInFilter(field_name='equipment_name', lookup_expr='in')

    class Meta:
        model = Equipment
        fields = ['audience_number']
