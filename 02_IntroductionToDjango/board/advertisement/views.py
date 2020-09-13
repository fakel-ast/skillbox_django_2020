from django.shortcuts import render


def course_view(request, id_course, *args, **kwargs):
    return render(request, "advertisement/" + str(id_course) + ".html")


def home_view(request, *args, **kwargs):
    dict_courses = [
        {"python_course": "Курс по питону"},
        {"java_course": "Курс по джаве"},
        {"web_developer": "Курс по веб разработке"},
        {"frontend": "Курс по фронтэенд разработке"},
        {"ios_developer": "Курс по ios разработке"},
    ]
    return render(request, "advertisement/home.html", context={"dict_courses": dict_courses})
