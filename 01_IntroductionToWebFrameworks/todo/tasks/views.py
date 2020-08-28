from random import shuffle

from django.http import HttpResponse
from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        do_list = ["Встать пораньше", "Почистить зубы", "Попить чаю", "Включить ПК", "Написать 5 надписей",
                   "Установить python", "Установить django", "Запустить сервер", "Порадоваться результату"]
        shuffle(do_list)
        return HttpResponse("<ul>" + "".join(["<li>" + do_list.pop() + "</li>" for i in range(5)]) + "</ul>")


