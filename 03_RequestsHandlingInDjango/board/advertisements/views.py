from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


company_info = [
    {
        "address": "Vologda, Dalinaya 32",
        "number": "8976-543-21-00",
        "email": "email@ya.ru",
        "name": "ООО Починка Стульев",
        "description": "Делаем стулья просто и быстро, и удобно. Покупайте только у нас!!!"
    }
]


class HomeView(View):

    advertisements_info = {
        "regions": ["Вологда", "Москва", "Ярославль", "Кириллов"],
        "categories": ["личные вещи", "транспорт", "хобби", "отдых"],
    }

    def get(self, request):
        return render(request, 'advertisements/home.html', context={"advertisements_info": self.advertisements_info})


class ContactsView(View):
    info = []
    for company in company_info:
        for key, value in company.items():
            if key in ["address", "number", "email"]:
                info.append((key, value))

    def get(self, request):
        return render(request, 'advertisements/contacts.html', context={"company_info": self.info})


class AboutView(View):
    info = []
    for company in company_info:
        for key, value in company.items():
            if key in ["name", "description"]:
                info.append((key, value))

    def get(self, request):
        return render(request, 'advertisements/about.html', context={"company_info": self.info})


class AdvertisementsListsView(View):

    counter = {
        "count_request": 0
    }

    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура',
        'Покупка лома за дорого',
        'Продажа волос за дешиво',
    ]

    def get(self, request):
        self.counter["count_request"] += 1
        return render(request, 'advertisements/advertisements_detail.html',
                      context={'advertisements': self.advertisements,
                               'count_request': self.counter["count_request"]})

    def post(self, request):
        return HttpResponse('Запись успешно создана')
