from django.urls import path

from .import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("<slug:id_course>/", views.course_view, name=""),

]
