from django.urls import path
from . import views

# The urls for my home app
urlpatterns = [
    path('', views.index, name='home'),
]
