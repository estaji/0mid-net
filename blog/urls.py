from django.urls import path
from .views import BlogView, ArticleView, TagView, TagsListView, ArticlePreview


app_name = "blog"
urlpatterns = [
    path(
        '',
        BlogView.as_view(template_name="blog/home.html"),
        name='home',
    ),
    path(
        'page/<int:page>',
        BlogView.as_view(template_name="blog/home.html"),
        name="home"),
    path(
        'tags',
        TagsListView.as_view(template_name="blog/tagslist.html"),
        name='tagslist',
    ),
    path(
        '<slug:slug>',
        ArticleView.as_view(template_name="blog/article.html"),
        name='article',
    ),
    path(
        'tag/<slug:slug>',
        TagView.as_view(template_name="blog/tag.html"),
        name='tag',
    ),
    path(
        'tag/<slug:slug>/page/<int:page>',
        TagView.as_view(template_name="blog/tag.html"),
        name='tag',
    ),
    path(
        'preview/<slug:slug>',
        ArticlePreview.as_view(template_name="blog/article.html"),
        name='preview',
    ),
]
