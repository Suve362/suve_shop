from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from suve_auth.forms import LoginForm
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



