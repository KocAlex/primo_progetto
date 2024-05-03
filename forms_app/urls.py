from django.urls import path
from forms_app.views import contatti
app_name = "forms_app"
urlpatterns = [
    path("contattaci/", contatti, name = "contattaci")
]
