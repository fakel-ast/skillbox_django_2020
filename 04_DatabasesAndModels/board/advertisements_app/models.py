from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    date_pub = models.DateTimeField(verbose_name='Дата Публикации')
    date_end_pub = models.DateTimeField(verbose_name='Дата окончания публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Автор')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Категория')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                                related_name='advertisements', verbose_name='Тип')

    def __str__(self):
        return self.title


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Имейл')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Катерогия')

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип объявления')

    def __str__(self):
        return self.name
