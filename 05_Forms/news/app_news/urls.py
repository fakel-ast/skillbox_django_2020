from django.urls import path

from app_news.views import AdvertisementView

urlpatterns = [
    path('', AdvertisementView.as_view(), name='create_advertisement')
]
