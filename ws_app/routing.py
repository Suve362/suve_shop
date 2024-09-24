from django.urls import path

from suve_auth.urls import app_name
from .consumers import MyAppConsumer


websocket_urlpatterns = [
    path('ws/app/', MyAppConsumer.as_asgi(), name='ws_app')
]