from django.urls import path
from prima_app.views import homepage, welcome, lista, variabili, index, chi_siamo
app_name = "prima_app"
urlpatterns = [
    path('homepage', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),
    path('lista', lista, name="lista"),
    path('variabili', variabili, name="variabili"),
    path('chi_siamo', chi_siamo, name="chi_siamo"),
    path('', index, name="index"),

]
