from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_houses, name='houses'),
]
