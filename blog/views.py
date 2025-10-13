from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from resume.mixins import GlobalContextMixin

from blog.models import Article, BlogConfig, Tag


class BlogView(GlobalContextMixin, ListView):
    """View for blog main page, list of all articles"""

    queryset = Article.objects.published()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["blog_settings"] = BlogConfig.objects.first()

        return context


class ArticleView(GlobalContextMixin, DetailView):
    """View for an article"""

    def get_object(self):
        slug = self.kwargs.get("slug")
        article = get_object_or_404(Article.objects.published(), slug=slug)

        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["blog_settings"] = BlogConfig.objects.first()

        return context


class TagView(GlobalContextMixin, ListView):
    """View for tag page, list of articles for a tag"""

    paginate_by = 5

    def get_queryset(self):
        global tag
        slug = self.kwargs.get("slug")
        tag = get_object_or_404(Tag.objects.all(), slug=slug)

        return tag.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tag"] = tag
        context["blog_settings"] = BlogConfig.objects.first()

        return context


class TagsListView(GlobalContextMixin, ListView):
    """View for all tags list"""

    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["blog_settings"] = BlogConfig.objects.first()

        return context


class ArticlePreview(LoginRequiredMixin, GlobalContextMixin, DetailView):
    """Preview an article before publishing just for admins"""

    def get_object(self):
        slug = self.kwargs.get("slug")
        article = get_object_or_404(Article, slug=slug)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["blog_settings"] = BlogConfig.objects.first()

        return context