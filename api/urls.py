from django.urls import path
from api.views import *

app_name = "api"
urlpatterns = [
    path('', index, name='index'),
    path('todos', todos_view, name='todos'),
    path('spotify-login/', spotify_login, name='spotify_login'),
    path('spotify-callback/', spotify_callback, name='spotify_callback'),
    path('spotify-success/', spotify_success, name='spotify_success'),
    path('spotify/', spotify, name='test_spotify'),


]