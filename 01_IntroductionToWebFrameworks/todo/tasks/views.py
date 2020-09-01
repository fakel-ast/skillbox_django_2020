from random import shuffle

from django.http import HttpResponse
from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        do_list = ["Встать пораньше", "Включить ПК", "Установить django",
                   "Почистить зубы", "Написать 5 надписей", "Запустить сервер",
                   "Попить чаю", "Установить python", "Порадоваться результату"]

        shuffle(do_list)
        
        return HttpResponse("<ul><li>" + "</li><li>".join(do_list[:5]) + "</li></ul>")


