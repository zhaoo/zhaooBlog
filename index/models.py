from django.db import models
from mdeditor.fields import MDTextField

class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    name = models.CharField('标签', max_length=30)
    number = models.IntegerField(verbose_name='数目', default=1)

    def __str__(self):
        return self.name

class Article(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    title = models.CharField('标题', max_length=150)
    content = MDTextField('内容')
    abstract = models.TextField('摘要', max_length=300, null=True, blank=True)
    post_time = models.DateTimeField('发布时间')
    views = models.IntegerField('浏览量', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    keywords = models.CharField('关键词', max_length=300, null=True, blank=True)

    def content_cut(self):
        if len(str(self.content))>300:
            return '{}...' .format(str(self.content)[0:300])
        else:
            return str(self.content)
    
    def get_absolute_url(self):
        return '/article/%s/' % (self.id)

    content_cut.short_description = u"内容"

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
    nicname = models.CharField(verbose_name='昵称', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    email = models.EmailField(verbose_name='邮箱', max_length=50, null=True)
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:10]

class Setting(models.Model):
    class Meta:
        verbose_name = '设置'
        verbose_name_plural = verbose_name
    title = models.CharField('博客标题', max_length=150)
    description = models.CharField('博客描述', max_length=300, null=True, blank=True)
    keywords = models.CharField('博客关键词', max_length=300, null=True, blank=True)
