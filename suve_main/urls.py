from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('page/<int:page_id>/', views.pages, name='pages'),
    path('main/', views.main, name='redirect_to_main'),
    path('products/', views.products_page, name='products'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('cart/', views.cart_page, name='cart'),
    path('login/', views.login, name='login')

]