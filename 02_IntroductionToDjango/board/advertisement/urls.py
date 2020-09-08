from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("python_course", views.python_course, name="python_course"),
    path("java_course", views.java_course, name="java_course"),
    path("web_developer", views.web_developer_course, name="web_developer_course"),
    path("frontend", views.frontend_course, name="frontend_course"),
    path("ios_developer", views.ios_developer_course, name="ios_developer_course"),

]