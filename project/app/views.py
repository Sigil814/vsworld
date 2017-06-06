from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def eleven(request):
    return HttpResponse("Hello")

def page(request):
    return render(request, 'app/page.html')
