from django.urls import path
from . import views

urlpatterns = [
    path('', views.coin_list, name='coin_list'),
    path('gold/', views.gold_list, name='gold_list')
]
