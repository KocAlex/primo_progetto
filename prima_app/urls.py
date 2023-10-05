from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili, index
app_name = "prima_app"
urlpatterns = [
            path("", index, name = "index"),
            path("homepage", homepage, name = "homepage"),
            path("welcome", welcome, name = "welcome"),
            path("lista", lista, name = "lista"),
            path("chi_siamo", chi_siamo, name = "chi_siamo"),
            path("variabili", variabili, name = "variabili"),
            ]