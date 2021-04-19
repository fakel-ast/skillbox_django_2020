from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from advertisements_app.models import Advertisement


class Command(BaseCommand):
    help = u'Создание случайного пользователя'

    def handle(self, *args, **kwargs):
        objs = (Advertisement(title=f'adv {i}') for i in range(500000))
        Advertisement.objects.bulk_create(objs)
