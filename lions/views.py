from django.shortcuts import render
from django.http import HttpResponse
from .models import Lion


def index(request):
    lions = Lion.objects.all()
    return render(request, 'index.html', {'lions': lions})
