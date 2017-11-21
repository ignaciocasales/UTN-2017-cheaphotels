from django.shortcuts import render
from django.views import generic


class IndexView(generic.ArchiveIndexView):
    template_name = 'bookings/index.html'
