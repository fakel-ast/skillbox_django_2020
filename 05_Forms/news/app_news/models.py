from django.db import models


class Advertisement(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()

