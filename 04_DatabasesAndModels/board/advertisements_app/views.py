from advertisements_app.models import *
from django.views.generic import ListView, DetailView


class AdvertisementsListView(ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisements_list'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    context_object_name = 'advertisement'
