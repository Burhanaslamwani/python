# Generated by Django 2.0.1 on 2018-01-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180129_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='model_pic',
            field=models.ImageField(default='blog/static/blog/assets/img/header-2.jpg', upload_to='documents'),
        ),
    ]
