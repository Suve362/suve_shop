from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'suve_auth'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('reg_done/', views.register_done, name='register_done'),
    ]