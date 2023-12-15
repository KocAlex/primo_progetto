from django.urls import path
from voti.views import elencoMaterie, dizionario, media, ultimaPagina
app_name = "voti"
urlpatterns = [
            path("view_a", elencoMaterie, name = "view_a"),
            path("view_b", dizionario, name = "view_b"),
            path("view_media", media, name = "view_media"),
            path("view_ultimaPagina", ultimaPagina, name = "view_ultimaPagina")
            ]