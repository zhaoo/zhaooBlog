from django.contrib import admin
from index.models import Article, Tag, Comment, Setting

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_cut', 'abstract', 'post_time', 'views']
    list_display_links = ('id', 'title')

    def save_model(self, request, obj, form, change):
            obj.save()
            obj_tags_list = obj.tags.all()
            for obj_tag in obj_tags_list:
                obj_tag.number = obj_tag.article_set.count()
                obj_tag.save()

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'article','nicname', 'comment_time']
    list_display_links = ('id', 'content', 'article', 'nicname', 'comment_time')

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords', 'description']
    list_display_links = ('title', 'keywords', 'description')

admin.site.site_header = 'zhaoo'
admin.site.site_title = 'zhaoo'
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Setting, SettingAdmin)
