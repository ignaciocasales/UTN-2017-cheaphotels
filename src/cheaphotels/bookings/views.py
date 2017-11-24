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
        city = request.POST['city']
        pax = request.POST['pax']
        max_price = request.POST['max_price']
        properties = Property.objects.all()

        if not city.__eq__('None'):
            properties = properties.filter(city=city)

        if not pax.__eq__('None'):
            properties = properties.filter(max_pax__gte=pax)

        if max_price is not '':
            properties = properties.filter(daily_cost__lte=max_price)

        context = {'properties': properties}
        return render(request, 'bookings/hotel-search-results.html', context)


def hotel_details(request, property_id):
    try:
        requested_property = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        raise Http404("Not Found")
    return render(request, 'bookings/hotel-details.html', {'property': requested_property})
