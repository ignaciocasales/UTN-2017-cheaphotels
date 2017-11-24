from django.conf.urls import url

from . import views

app_name = 'bookings'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.hotel_search_results, name='hotel_search_results'),
    url(r'^property/([0-9]+)/$', views.hotel_details, name='hotel_details')
]
