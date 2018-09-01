from django.contrib.syndication.views import Feed
from django.urls import reverse
from index.models import Article

class RssFeed(Feed):
    title = "zhaoo"
    link = "/rss/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('index:article', args=[item.id, ])
