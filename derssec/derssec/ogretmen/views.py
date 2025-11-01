from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def ogretmenanasayfa(request):
  template = loader.get_template('ogretmenana.html')
  return HttpResponse(template.render())
