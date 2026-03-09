from django.urls import path

import forms_app
from forms_app.views import *
app_name = "forms_app"
urlpatterns = [
    path('contattaci/', contatti, name="contatti"),
    path('lista_contatti', lista_contatti, name="lista_contatti"),
    path('elimina_contatto/<int:pk>', elimina_contatto, name="elimina_contatto"),
    path('modifica_contatto/<int:pk>', modifica_contatto, name="modifica_contatto"),
]
