from django.urls import re_path

from . import chatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_id>[0-9a-fA-F\-]+)/$", chatConsumer.ChatConsumer.as_asgi()),

    # re_path(r"ws/chat/(?P<room_id>[^/]+)/$",chatConsumer.ChatConsumer.as_asgi(),)
    # re_path(r"ws/chat/(?P<room_id>\w+)/$",chatConsumer.ChatConsumer.as_asgi(),)
]