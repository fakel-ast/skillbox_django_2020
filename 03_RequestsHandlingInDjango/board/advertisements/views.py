from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView


count_request = 0


class HomeView(TemplateView):
    template_name = "advertisements/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regions"] = ["Вологда", "Москва", "Ярославль", "Кириллов"]
        context["categories"] = ["личные вещи", "транспорт", "хобби", "отдых"]
        return context


class ContactsView(TemplateView):
    template_name = "advertisements/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address"] = "Vologda, Dalinaya 32"
        context["number"] = "8976-543-21-00"
        context["email"] = "email@ya.ru"
        return context


class AboutView(TemplateView):
    template_name = "advertisements/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ООО Починка Стульев"
        context["description"] = "Делаем стулья просто и быстро, и удобно. Покупайте только у нас!!!"
        return context


class AdvertisementsListsView(TemplateView):
    template_name = "advertisements/advertisements_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["advertisements"] = [
            'Мастер на час', 'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]

        context["count_request"] = count_request
        return context

    def post(self, request, *args, **kwargs):
        global count_request
        count_request += 1
        return HttpResponse('Объявление успешно создана')
