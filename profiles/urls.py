from django.urls import path
from . import views

# The urls for my profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
    path('add/<int:house_id>/', views.add_subscription, name='add_subscription'),
    path('delete/<int:subscription_id>/', views.delete_subscription, name='delete_subscription'),
]
