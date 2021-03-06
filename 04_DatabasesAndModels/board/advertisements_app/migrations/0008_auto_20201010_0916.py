# Generated by Django 2.2 on 2020-10-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0007_auto_20201008_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_end_pub',
            field=models.DateTimeField(verbose_name='Дата окончания публикации'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_pub',
            field=models.DateTimeField(verbose_name='Дата Публикации'),
        ),
        migrations.AlterField(
            model_name='advertisementtype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Тип объявления'),
        ),
    ]
