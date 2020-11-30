from django.urls import path
from . import views
from .webhooks import webhook

# The urls for my payment app
urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment_success/<int:payment_number>', views.payment_success, name='payment_success'),
    path('wh/', webhook, name='webhook'),
]