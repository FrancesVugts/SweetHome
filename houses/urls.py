from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_houses, name='houses'),
    path('<house_id>', views.house_info, name='house_info'),
]
