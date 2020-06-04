import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='static/web/media/')
    resume = models.TextField()
    pub_date = models.DateTimeField('date published')
    content = HTMLField('Content')

    def published_on_the_future(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) > self.pub_date > now

    def __str__(self):
        return f"{self.title}"
