from django.urls import path
from . import views

urlpatterns = [
    path('', views.Accueil, name='Accueil'),
    path('Contact/', views.Contact, name='Contact'),
    path('Services/', views.Services, name='Services'),
    path('Produits/', views.Produits, name='Produits'),
    path('Produits/<name>/', views.prod, name='prod'),
]
