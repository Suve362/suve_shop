from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from suve_auth.forms import LoginForm, RegisterForm, ProfileForm, UserPasswordChangeForm, UserPasswordReset
from suve_main.models import Routes


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, email=cd['email'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main'))
#     else:
#         form = LoginForm()
#     return render(request, '/opt/python_projects/suve_shop/suve_auth/templates/login.html', {'form': form})
#
#
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('auth:login'))


class LoginUser(LoginView):

    form_class = LoginForm
    template_name = 'login.html'

    # def get_success_url(self):
    #     return reverse_lazy('main')


class RegisterUser(CreateView):

    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('auth:register_done')


class RegisterDone(TemplateView):
    template_name = 'register_done.html'


class ProfileUser(LoginRequiredMixin, UpdateView):

    model = get_user_model()
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('auth:profile')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChange(PasswordChangeView):

    model = get_user_model()
    form_class = UserPasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('auth:password_change_done')


class UserPasswordResetView(PasswordResetView):

    model = get_user_model()
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    form_class = UserPasswordReset
    success_url = reverse_lazy('auth:password_reset_done')




