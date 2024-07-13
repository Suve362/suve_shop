from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('page/<int:page_id>/', views.pages, name='pages'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),

]