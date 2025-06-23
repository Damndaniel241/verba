from django.urls import path
from .views import create_room_id

urlpatterns = [
    path("create-room-id/",create_room_id),
]