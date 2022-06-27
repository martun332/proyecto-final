from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template

# Create your views here.

def inicio(request):
    template = loader.get_template("index.html")
    render = Template.render({})
    return HttpResponse(render)