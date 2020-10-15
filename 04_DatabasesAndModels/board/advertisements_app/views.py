from advertisements_app.models import Advertisement

from django.views.generic import DetailView, ListView


class AdvertisementsListView(ListView):
    model = Advertisement
    template_name = 'advertisements_app/advertisement_list.html'
    context_object_name = 'advertisements_list'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    context_object_name = 'advertisement'
