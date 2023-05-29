from django.urls import re_path
from .consumers import MyConsumer

websocket_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>\w+)/$', MyConsumer.as_asgi()),
]
