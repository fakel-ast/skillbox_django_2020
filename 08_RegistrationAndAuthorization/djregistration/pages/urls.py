from django.urls import path

from pages import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
