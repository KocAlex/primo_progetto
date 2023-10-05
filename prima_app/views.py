from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def welcome(request):
    return render(request, "welcome.html")

def lista(request):
    return render(request, "lista.html")

def chi_siamo(request):
    return render(request, "chi_siamo.html")