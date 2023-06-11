from django.urls import re_path, path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/room/', MyConsumer.as_asgi()),
]
