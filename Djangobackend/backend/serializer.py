from rest_framework import serializers
from .models import Room, User, Equipment, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'audience_number', 'reservation_start', 'reservation_end']

    def validate(self, data):
        """Велосипед"""
        if data['reservation_end'] < data['reservation_start']:
            raise serializers.ValidationError("reservation_end must occur after reservation_start")
        if Reservation.objects.filter(reservation_end__gte=data['reservation_start'], reservation_start__lte=data['reservation_start']):
            raise serializers.ValidationError("time line crossing")
        if Reservation.objects.filter(reservation_start__lte=data['reservation_end'], reservation_end__gte=data['reservation_end']):
            raise serializers.ValidationError("time line crossing")
        if Reservation.objects.filter(reservation_start__lte=data['reservation_start'], reservation_end__gte=data['reservation_end']):
            raise serializers.ValidationError("time line crossing")

        return data
