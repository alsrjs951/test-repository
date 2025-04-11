from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def mingeon(request):
    return render(request, 'main/mingeon.html')

def dohun(request):
    return render(request, 'main/dohun.html')