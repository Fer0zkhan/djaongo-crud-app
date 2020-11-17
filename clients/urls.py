from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('client/home/', home, name='home'),
    path('client/add/', add_client, name='add_client'),
    path('client/<int:pk>/edit/', edit_client, name='edit_client'),
    path('client/<int:pk>/delete/', delete_client, name='delete_client'),

]
