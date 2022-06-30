from django.contrib import admin
from .models import Article, Tag, Configuration


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'language',
        'article_tags',
        'published_modified'
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'posts_count')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Configuration)
