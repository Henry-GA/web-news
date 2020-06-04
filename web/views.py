from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import NewsForm
from .models import News


# Create your views here.

def index(request):
    new = News.objects.filter(pub_date__lte=timezone.now())
    return render(request, 'web/index.html', {'news': new})


def news(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    return render(request, 'web/news.html', {'new': new})
