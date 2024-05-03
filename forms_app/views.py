from django.shortcuts import render
from .forms import FormContatto
# Create your views here.
def contatti(request):
    form = FormContatto()
    context = {"form":form}
    return render(request, "contatto.html", context)