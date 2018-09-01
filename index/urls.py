from django.urls import path
from . import views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from index.models import Article
from index.feeds import RssFeed

app_name = 'index'

hander404 = 'views.page_not_found'

hander505 = 'views.page_errors'

sitemaps = {
    'index': GenericSitemap({'queryset': Article.objects.all()}, priority=0.5),
}

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article, name='article'),
    path('tags/', views.tags, name='tags'),
    path('tags/<str:name>', views.tag, name='tag'),
    path('archive/', views.archive, name='archive'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('rss/', RssFeed(), name='rss'),
]
