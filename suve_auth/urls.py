from django.contrib.messages import success
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
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
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                                             success_url = reverse_lazy('auth:password_reset_complete')),
                                                                             name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    ]