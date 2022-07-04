from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('recharge/', views.recharge, name='recharge'),
    path('rechargeok/', views.rechargeok, name='rechargeok'),
]