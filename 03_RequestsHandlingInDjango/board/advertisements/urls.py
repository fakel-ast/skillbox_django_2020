from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('contacts/', views.contacts_view, name='contacts_detail'),
    path('about/', views.about_view, name='about_detail'),
    path('categories/', views.categories_list_view, name='categories_detail'),
    path('regions/', views.RegionsList.as_view(), name='regions_detail'),
]
