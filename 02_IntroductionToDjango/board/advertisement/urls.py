from django.urls import path

from .import views


urlpatterns = [
    path("", views.home_views, name="home"),
    path("python_course", views.python_course_views, name="python_course"),
    path("java_course", views.java_course_views, name="java_course"),
    path("web_developer", views.web_developer_course_views, name="web_developer_course"),
    path("frontend", views.frontend_course_views, name="frontend_course"),
    path("ios_developer", views.ios_developer_course_views, name="ios_developer_course"),
]
