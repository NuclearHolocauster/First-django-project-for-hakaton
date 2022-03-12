from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


app_name = 'backend'
urlpatterns = [
    path('user/create', UserCreateView.as_view()),
    path('room/create', RoomCreateView.as_view()),
    path('equipment/create', EquipmentCreateView.as_view()),
    path('reservation/create', ReservationCreateView.as_view()),
    path('user/all', UserListView.as_view()),
    path('room/all', RoomListView.as_view()),
    path('equipment/all', EquipmentListView.as_view()),
    path('reservation/all', ReservationListView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('room/<int:pk>', RoomDetailView.as_view()),
    path('equipment/<int:pk>', EquipmentDetailView.as_view()),
    path('reservation/<int:pk>', ReservationDetailView.as_view()),
    path('equipment/all?audience_number=<int:pk>', EquipmentListView.as_view())
]
