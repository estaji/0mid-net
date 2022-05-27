from django.views.generic import ListView, TemplateView
from .models import Article


class BlogView(ListView):
    """View for blog main page"""
    queryset = Article.objects.published()


class ArticleView(TemplateView):
    """View for an article"""
    pass
