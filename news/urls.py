from django.urls import path
from .views import home, articoloDetailView

app_name = 'news'

urlpatterns = [
    path("", home, name = "homeview"),
    path("articoli/<int:pk>", articoloDetailView, name = "articolo_detail"),
]