from django.shortcuts import render

from django.http import HttpResponse

from django.template import Context, loader


def index(request):

    return render(request, "../templates/index.html")

def comunidad(request):

    return render(request, "../templates/comunidad.html")

def foro(request):

    return render(request, "../templates/foro.html")