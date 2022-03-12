from django.urls import path
from .views import *


app_name = 'backend'
urlpatterns = [
    path('user/create', UserCreateView.as_view()),
    path('room/create', RoomCreateView.as_view()),
    path('equipment/create', EquipmentCreateView.as_view()),
    path('user/all', UserListView.as_view()),
    path('room/all', RoomListView.as_view()),
    path('equipment/all', EquipmentListView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('room/<int:pk>', RoomDetailView.as_view()),
    path('equipment/<int:pk>', EquipmentDetailView.as_view())
]
