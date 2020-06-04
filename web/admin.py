from django.contrib import admin

from .models import News


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(News, NewsAdmin)
