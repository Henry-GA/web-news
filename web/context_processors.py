from django.utils import timezone

from web.models import News


def add_variable_to_context(self):
    recent_news = News.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
    return {
        'recent_news': recent_news
    }
