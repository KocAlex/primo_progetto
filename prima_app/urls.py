from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo
app_name = "prima_app"
urlpatterns = [
            path("", homepage, name = "homepage"),
            path("welcome", welcome, name = "welcome"),
            path("lista", lista, name = "lista"),
            path("chi_siamo", chi_siamo, name = "chi_siamo"),
            ]