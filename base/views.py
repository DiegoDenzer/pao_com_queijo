from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):
    template = 'base/home.html'
    return render(request, template_name=template)