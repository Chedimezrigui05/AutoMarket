from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('commander/', views.commander, name='commander'),
]
