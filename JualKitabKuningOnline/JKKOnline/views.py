from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
   
def JKKOnline(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def JKKOnlines(request):
    Layout = loader.get_template('detil.html')
    return HttpResponse(Layout.render())
# def JKKOnline(request):
#     return HttpResponse("<h1> DISINI JUAL KITAB KUNING<h1>")
