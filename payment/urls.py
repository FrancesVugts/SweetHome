from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment_success/<payment_number>', views.payment_success, name='payment_success'),
]