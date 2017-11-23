from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic


def index(request):
    return render(request, 'bookings/index.html')
