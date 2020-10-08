from django.contrib import admin
from advertisements_app.models import *


@admin.register(Advertisement)
class Advertisements(admin.ModelAdmin):
    pass


@admin.register(AdvertisementAuthor)
class Author(admin.ModelAdmin):
    pass


@admin.register(AdvertisementCategory)
class Category(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class Type(admin.ModelAdmin):
    pass
