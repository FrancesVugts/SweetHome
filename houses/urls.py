from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_houses, name='houses'),
    path('<int:house_id>/', views.house_info, name='house_info'),
    path('add/', views.add_house, name='add_house'),
]
