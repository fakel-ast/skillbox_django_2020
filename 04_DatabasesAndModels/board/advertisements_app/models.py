from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    date_pub = models.DateTimeField(verbose_name='Дата Публикации')
    date_end_pub = models.DateTimeField(verbose_name='Дата окончания публикации', blank=True, null=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement_author', verbose_name='Автор')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, on_delete=models.CASCADE,
                                 related_name='advertisement_category', verbose_name='Категория')
    advertisement_type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                                           related_name='advertisement_type', verbose_name='Тип')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Е-mail')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Автор объявления'
        verbose_name_plural = 'Авторы объявлений'

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория объявления'
        verbose_name_plural = 'Катерогии объявлений'

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип объявления')

    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявлений'

    def __str__(self):
        return self.name
