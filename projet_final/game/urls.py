from django.urls import path
from . import views

urlpatterns = [
    path('', views.memory_game, name='memory_game'),
]
