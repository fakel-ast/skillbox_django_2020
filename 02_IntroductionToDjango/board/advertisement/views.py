from django.shortcuts import render


dict_courses = {
    "courses":
    [
        {
            "slug": "python_course",
            "title": "python",
            "text": "Курс по питону",
            "price": "3 ханрдед бакса",
            "img": "/media/image/python.png",
            "link_about": "https://skillbox.ru/course/profession-python/",
        },

        {
            "slug": "frontend_course",
            "title": "frontend",
            "text": "Курс по фронтэнд",
            "price": "4 ханрдед бакса",
            "img": "/media/image/frontend.png",
            "link_about": "https://skillbox.ru/course/profession-frontend/",
        },
        {
            "slug": "java_course",
            "title": "java",
            "text": "Курс по java",
            "price": "5 ханрдед бакса",
            "img": "/media/image/java.png",
            "link_about": "https://skillbox.ru/course/profession-java/",
        },
        {
            "slug": "web_developer_course",
            "title": "web_developer",
            "text": "Курс по web разработке",
            "price": "6 ханрдед бакса",
            "img": "/media/image/web_developer.png",
            "link_about": "https://skillbox.ru/course/profession-webdev/",
        },
        {
            "slug": "ios_developer_course",
            "title": "ios_developer",
            "text": "Курс по ios разработке",
            "price": "7 ханрдед бакса",
            "img": "/media/image/ios_developer.png",
            "link_about": "https://skillbox.ru/course/profession-ios-developer/",
        }
    ]
}


def advertisement_course_detail_view(request, course_slug, *args, **kwargs):
    link_course = [dict_course for dict_course in dict_courses["courses"] if course_slug in dict_course.values()][0]
    print(link_course)
    return render(request, "advertisement/advertisement_course_detail.html",
                  context={"course": link_course})


def home_view(request, *args, **kwargs):
    return render(request, "advertisement/home.html", context={"dict_courses": dict_courses["courses"]})
