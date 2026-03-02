from django.urls import path
from forms_app.views import *
app_name = "forms_app"
urlpatterns = [
    path('contattaci/', contatti, name="contatti"),
    path('lista_contatti', lista_contatti, name="lista_contatti"),
]
