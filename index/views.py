from django.shortcuts import render
from index.models import Article, Tag, Comment, Setting
import markdown
from django.http import HttpResponse
from index.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    articleList = Article.objects.order_by("-post_time").all()
    for article in articleList:
        article.content = markdown.markdown(article.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    paginator = Paginator(articleList, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(pk=id)
    article.content = markdown.markdown(article.content,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    article.views += 1
    Article.objects.filter(pk=id).update(views=article.views)
    return render(request, 'article.html', {'article': article})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})

def tag(request, name):
    tag = Tag.objects.filter(name=name).first()
    articleList = tag.article_set.order_by("-post_time").all()
    paginator = Paginator(articleList, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'tag.html', {'articles': articles, 'tag': tag})

def archive(request):
    articles = Article.objects.order_by('-post_time').all()
    return render(request, 'archive.html', {'articles': articles})

def add_comment(request):
    comment = CommentForm(request.POST)
    if comment.is_valid():
        comment.save()
        return HttpResponse('{"status":1, "msg":"评论成功"}', content_type='application/json')
    else:
        return HttpResponse('{"status":-1, "msg":"评论失败"}', content_type='application/json')

def page_not_found(request):
    return render(request, '404.html')

def page_errors(request):
    return render(request, '500.html')
