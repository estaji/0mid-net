from django.views.generic import ListView, TemplateView
from .models import Article, Configuration


class BlogView(ListView):
    """View for blog main page, list of all articles"""
    queryset = Article.objects.published()
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Configuration.objects.first()
        return context


class ArticleView(TemplateView):
    """View for an article"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Configuration.objects.first()
        return context
