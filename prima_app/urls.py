from django.urls import path
from prima_app.views import homepage, welcome, lista, variabili, index
app_name = "prima_app"
urlpatterns = [
    path('homepage', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),
    path('lista', lista, name="lista"),
    path('variabili', variabili, name="variabili"),
    path('', index, name="index"),

]
