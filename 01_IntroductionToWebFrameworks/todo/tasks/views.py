from django.http import HttpResponse

from django.views import View

from random import choice

do_list = ["Встать пораньше", "Почистить зубы", "Попить чаю", "Включить ПК", "Написать 5 надписей",
           "Установить python", "Установить django", "Запустить сервер", "Порадоваться результату"]


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        temp_list = do_list[:]
        return HttpResponse('<ul>'
                            f'<li>{temp_list.pop(temp_list.index(choice(temp_list)))}</li>'
                            f'<li>{temp_list.pop(temp_list.index(choice(temp_list)))}</li>'
                            f'<li>{temp_list.pop(temp_list.index(choice(temp_list)))}</li>'
                            f'<li>{temp_list.pop(temp_list.index(choice(temp_list)))}</li>'
                            f'<li>{temp_list.pop(temp_list.index(choice(temp_list)))}</li>'
                            '</ul>')
