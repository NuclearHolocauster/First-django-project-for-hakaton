from rest_framework import generics
from .serializer import *
from .models import Room, User, Equipment
from django_filters.rest_framework import DjangoFilterBackend
from .services import EquipmentFilter


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializer


class EquipmentCreateView(generics.CreateAPIView):
    serializer_class = EquipmentSerializer


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EquipmentListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = EquipmentFilter


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class RoomEquipmentView(generics.ListAPIView):
    serializer_class = EquipmentSerializer

