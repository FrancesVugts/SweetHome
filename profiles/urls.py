from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add/<house_id>/', views.add_subscription, name='add_subscription'),
]
