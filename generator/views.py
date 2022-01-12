from functools import cached_property
from django.shortcuts import render
import random
import generator

# from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def password(request):
    characters = list("abcdefghijklmnopqrsuvwxyz")
    generator_password = ""
    length = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFHIJKLMNOPQRSTUVWXYZ"))


    if request.GET.get("special"):
        characters.extend(list("!@$%^&*()"))


    if request.GET.get("numbers"):
        characters.extend(list("123456789"))

        
    for x in range(length):
        generator_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": generator_password})
