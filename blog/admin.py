from django.contrib import admin
from .models import Article, Tag, Configuration


def make_published(modeladmin, request, queryset):
    """Change selected article's status to published"""
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "Article published."
    else:
        message_bit = "Articles published."
    modeladmin.message_user(request, "{} {}".format(rows_updated, message_bit))
    make_published.short_description = "Publish selected articles"


def make_draft(modeladmin, request, queryset):
    """Change selected article's status to drafted"""
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = "Article drafted."
    else:
        message_bit = "Articles drafted."
    modeladmin.message_user(request, "{} {}".format(rows_updated, message_bit))
    make_draft.short_description = "Draft selected articles"


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'language',
        'article_tags',
        'slug',
        'published_modified'
    )
    list_filter = ('published', 'status', 'language')
    actions = [make_published, make_draft]
    search_fields = ('title', 'slug')
    ordering = ['status', '-published']


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'posts_count', 'slug')
    search_fields = ('title', 'slug')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Configuration)
