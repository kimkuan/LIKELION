from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')