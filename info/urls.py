from django.urls import path
from . import views

# The urls for my info app
urlpatterns = [
    path('', views.info, name='info'),
]
