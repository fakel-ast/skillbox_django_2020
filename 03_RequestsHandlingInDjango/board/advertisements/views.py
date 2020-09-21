from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'пирожки',
        'блины',
        'картошка',
    ]
    advertisements_2 = [
        'покупай и продавай',
        'ехали медведи на велосипеде',
        'внимание, внимание. важное объявление. очень важное.',
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1,
                                                                      'advertisements_2': advertisements_2})


def contacts_view(request, *args, **kwargs):
    return render(request, 'advertisements/contacts.html', context={'number': '8-800-708-19-45',
                                                                    'email': 'sales@company.com'})


def about_view(request, *args, **kwargs):
    return render(request, 'advertisements/about.html', {'name': 'Бесплатные объявления',
                                                         'description': 'Бесплатные объявления в вашем городе!'})


def categories_list_view(request, *args, **kwargs):
    categories = [
        'личные вещи',
        'транспорт',
        'хобби и отдых',
    ]

    return render(request, 'advertisements/categories.html', {'categories': categories})


class RegionsList(View):

    regions = [
        'Москва',
        'Московская область',
        'республика Алтай',
        'Вологодская область',
        ]

    def get(self, request):
        return render(request, 'advertisements/regions.html', {'regions': self.regions})

    def post(self, request):
        return HttpResponse('Сообщение успешно отправлено')
