from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('page/<int:page_id>/', views.pages, name='pages'),
    path('main/', views.main, name='redirect_to_main'),
    path('products/', views.products_page, name='products_page'),
    path('products/apple/', views.products_apple, name='products_apple'),
    path('products/apple/iphone/', views.products_apple_iphone, name='products_apple_iphone'),
    path('products/apple/ipad/', views.products_apple_ipad, name='products_apple_ipad'),
    path('products/apple/macbook/', views.products_apple_macbook, name='products_apple_macbook'),
    path('products/apple/mac/', views.products_apple_mac, name='products_apple_mac'),
    path('products/apple/watch/', views.products_apple_watch, name='products_apple_watch'),
    path('products/apple/airpods/', views.products_apple_airpods, name='products_apple_airpods'),
    path('products/samsung/', views.products_samsung, name='products_samsung'),
    path('products/samsung/smartphones/', views.products_samsung_smartphones, name='products_samsung_smartphones'),
    path('products/samsung/tablets/', views.products_samsung_tab, name='products_samsung_tab'),
    path('products/samsung/galaxybooks/', views.products_samsung_galaxybook, name='products_samsung_galaxybook'),
    path('products/samsung/watches/', views.products_samsung_watch, name='products_samsung_watch'),
    path('products/samsung/galaxybuds/', views.products_samsung_galaxybuds, name='products_samsung_galaxybuds'),
    path('products/tesla/', views.products_tesla, name='products_tesla'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('cart/', views.cart_page, name='cart'),
    path('login/', views.login, name='login'),
]



