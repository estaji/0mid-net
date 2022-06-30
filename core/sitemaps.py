from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Article, Tag


class StaticSitemap(Sitemap):
    """Create sitemap for static pages"""
    changefreq = 'monthly'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['resume', 'blog:home', 'blog:tagslist']

    def location(self, item):
        return reverse(item)


class ArticleSitemap(Sitemap):
    """Create sitemap for articles"""
    changefreq = "yearly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Article.objects.published()

    def location(self, obj):
        return '/blog/%s' % (obj.slug)

    def lastmod(self, obj):
        return obj.updated


class TagSitemap(Sitemap):
    """Create sitemap for tag page"""
    changefreq = "monthly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Tag.objects.all()

    def location(self, obj):
        return '/blog/tag/%s' % (obj.slug)
