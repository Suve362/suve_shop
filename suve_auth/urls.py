from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

app_name = 'suve_auth'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('reg_done/', views.RegisterDone.as_view(), name='register_done'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.PasswordChange.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    ]