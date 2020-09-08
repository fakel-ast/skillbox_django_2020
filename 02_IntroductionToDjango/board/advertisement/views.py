from django.shortcuts import render


def python_course(request, *args, **kwargs):
    return render(request, "advertisement/python_course.html", {})


def java_course(request, *args, **kwargs):
    return render(request, "advertisement/java_course.html", {})


def web_developer_course(request, *args, **kwargs):
    return render(request, "advertisement/web_developer.html", {})


def frontend_course(request, *args, **kwargs):
    return render(request, "advertisement/frontend.html", {})


def ios_developer_course(request, *args, **kwargs):
    return render(request, "advertisement/ios_developer.html", {})


def home(request, *args, **kwargs):
    return render(request, "advertisement/home.html", {})



