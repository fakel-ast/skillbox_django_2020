from django.urls import path

from .import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("<slug:course_slug>/", views.advertisement_course_detail_view, name="advertisement_course_detail"),
]
