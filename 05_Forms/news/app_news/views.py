from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from app_news.forms import AdvertisementForm
from app_news.models import Advertisement


class AdvertisementView(View):

    def get(self, request):

        form = AdvertisementForm()
        return render(request, 'app_news/create_advertisement.html', context={'form': form})

    def post(self, request):

        form = AdvertisementForm(request.POST)

        if form.is_valid():
            Advertisement.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_news/create_advertisement.html', context={'form': form})
