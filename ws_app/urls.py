from django.urls import path
from .views import WSView

app_name = 'ws_app'

urlpatterns = [
    path('app/', WSView.as_view(), name='ws_app')
]