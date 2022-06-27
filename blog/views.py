from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import prueba

# Create your views here.

def inicio(request):
    #template = loader.get_template("index.html")
    #render = template.render({})
    #return HttpResponse(render)
    return render(request, 'index.html', {})