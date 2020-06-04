from django.urls import path

from web import views

urlpatterns = [
    path('<int:news_id>', views.news, name='news'),
]