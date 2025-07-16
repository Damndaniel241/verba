from django.urls import path
from .views import create_room_id,get_messages

urlpatterns = [
    path("create-room-id/",create_room_id),
    path("messages/<str:room_id>/",get_messages)
]