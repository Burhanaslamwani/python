# Generated by Django 2.0.1 on 2018-01-29 06:27

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180129_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='model_pic',
            field=models.ImageField(default='blog/static/blog/assets/img/header-2.jpg', storage=django.core.files.storage.FileSystemStorage(location='C:/Users/burhan/Desktop/new log/Django/mysite/blog/static/blog/img/'), upload_to=''),
        ),
    ]