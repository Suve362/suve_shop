from django.urls import path, include
from . import views
from rest_framework import routers

from .views import SuveMainSetView


router = routers.DefaultRouter()
router.register(r'products', SuveMainSetView, basename='products')

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    # path('page/<int:page_id>/', views.pages, name='pages'),
    path('main/', views.main, name='redirect_to_main'),
    path('products/', views.ProductsPage.as_view(), name='products_page'),
    path('products/apple/', views.ProductsApple.as_view(), name='products_apple'),
    path('products/apple/iphone/', views.ProductsAppleIphone.as_view(), name='products_apple_iphone'),
    path('products/apple/ipad/', views.ProductsAppleIpad.as_view(), name='products_apple_ipad'),
    path('products/apple/macbook/', views.ProductsAppleMacbook.as_view(), name='products_apple_macbook'),
    path('products/apple/mac/', views.ProductsAppleMac.as_view(), name='products_apple_mac'),
    path('products/apple/watch/', views.ProductsAppleWatch.as_view(), name='products_apple_watch'),
    path('products/apple/airpods/', views.ProductsAppleAirpods.as_view(), name='products_apple_airpods'),
    path('products/samsung/', views.ProductsSamsung.as_view(), name='products_samsung'),
    path('products/samsung/smartphones/', views.ProductsSamsungSmartphones.as_view(), name='products_samsung_smartphones'),
    path('products/samsung/tablets/', views.ProductsSamsungTab.as_view(), name='products_samsung_tab'),
    path('products/samsung/galaxybooks/', views.ProductsSamsungGalaxybook.as_view(), name='products_samsung_galaxybook'),
    path('products/samsung/watches/', views.ProductsSamsungWatch.as_view(), name='products_samsung_watch'),
    path('products/samsung/galaxybuds/', views.ProductsSamsungGalaxybuds.as_view(), name='products_samsung_galaxybuds'),
    path('products/tesla/', views.ProductsTesla.as_view(), name='products_tesla'),
    path('contacts/', views.ContactsPage.as_view(), name='contacts'),
    path('cart/', views.CartPage.as_view(), name='cart'),
    path('api/', include(router.urls)),
]



