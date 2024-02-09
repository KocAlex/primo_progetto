from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path("", home, name = "homeview"),
    path("articoli/<int:pk>", articoloDetailView, name = "articolo_detail"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name = "giornalista_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name = "lista_articoli_giornalista"),
    path("lista_articoli/", listaArticoli, name = "lista_articoli"),
    path("query_base/", queryBase, name = "query_base"),
    path("api_giornalisti/", giornalisti_list_api, name = "api_giornalisti"),
    path("api_giornalista/<int:pk>", giornalista_api, name = "api_giornalista"),
    path("api_articoli/", articoli_list_api, name = "api_articoli"),
    path("api_articolo/<int:pk>", articolo_api, name = "api_articolo"),
]