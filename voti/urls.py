from django.urls import path
from voti.views import *
app_name = "voti"
urlpatterns = [
    path('', index, name="index"),
    path('lista_materie', view_a, name="lista_materie"),
    path('lista_voti_assenze', view_b, name="lista_voti_assenze"),
    path('lista_medie', view_c, name="lista_medie"),
    path('max_min_voti', view_d, name="max_min_voti"),
]
