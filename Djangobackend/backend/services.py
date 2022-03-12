from django_filters import rest_framework as filters
from .models import Equipment


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EquipmentFilter(filters.FilterSet):
    audience_id = CharFilterInFilter(field_name='audience_id', lookup_expr='in')

    class Meta:
        model = Equipment
        fields = ['audience_id']
