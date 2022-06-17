from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Article, Tag, Configuration


class BlogView(ListView):
    """View for blog main page, list of all articles"""
    queryset = Article.objects.published()
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Configuration.objects.first()
        return context


class ArticleView(DetailView):
    """View for an article"""

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)

        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Configuration.objects.first()
        return context


class TagView(ListView):
    """View for tag page, list of articles for a tag"""
    paginate_by = 7

    def get_queryset(self):
        global tag
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tag.objects.all(), slug=slug)
        return tag.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = tag
        context['settings'] = Configuration.objects.first()
        return context


class TagsListView(ListView):
    """View for all tags list"""
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Configuration.objects.first()
        return context
