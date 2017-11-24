from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.views import generic

from .models import City, Property


def index(request):
    cities = City.objects.all()
    context = {'cities': cities }
    return render(request, 'bookings/index.html', context)


def hotel_search_results(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        context = {'properties': properties}
        return render(request, 'bookings/hotel-search-results.html', context)
    if request.method == 'POST':
        properties = Property.objects.all()
        context = {'properties': properties}
        return render(request, 'bookings/hotel-search-results.html', context)


def hotel_details(request, property_id):
    try:
        requested_property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        raise Http404("Not Found")
    return render(request, 'bookings/hotel-details.html', {'property': requested_property})
