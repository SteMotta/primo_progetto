from django.urls import path
from news.views import *

app_name = "news"
urlpatterns = [
    path('', index, name='index'),
    path('homepage/', home, name='homepage'),
    path("articolo/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/", listaArticoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli")
]