from django.urls import path
from .views import HomeView, ArticleView


app_name = "blog"
urlpatterns = [
    path(
        '',
        HomeView.as_view(template_name="blog/home.html"),
        name='blog',
    ),
    path(
        'article/',
        ArticleView.as_view(template_name="blog/article.html"),
        name='article',
    ),
]
