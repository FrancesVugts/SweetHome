from django.urls import path
from . import views

# The urls for my contact app
urlpatterns = [
    path('', views.contact, name='contact'),
]
