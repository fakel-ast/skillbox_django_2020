from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('advertisements/', views.AdvertisementsListsView.as_view(), name="advertisements_list"),
    path('contacts/', views.ContactsView.as_view(), name='contacts_detail'),
    path('about/', views.AboutView.as_view(), name='about_detail'),
]
