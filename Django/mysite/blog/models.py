from django.db import models
import datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='C:/Users/burhan/Desktop/new log/Django/mysite/blog/static/blog/img/')

class Heading(models.Model):
    heading_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    body_text = models.CharField(max_length=5000, default=0)
    model_pic = models.ImageField(upload_to='documents', default = 'blog/static/blog/assets/img/header-2.jpg')

    def __str__(self):
        return self.heading_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Body(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    body_text = models.CharField(max_length=2000)
    def __str__(self):
        return self.body_text
    #votes = models.IntegerField(default=0)
# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
