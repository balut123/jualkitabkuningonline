from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
   
def Pemasaran(request):
    template = loader.get_template('ikbal.html')
    return HttpResponse(template.render())
