from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic.base import TemplateView

from resume.views import ResumeView
from blog.sitemaps import ArticleSitemap, StaticSitemap, TagSitemap


sitemaps = {
    "static": StaticSitemap(),
    "tag": TagSitemap(),
    "article": ArticleSitemap(),
}

urlpatterns = [
    path(
        "",
        ResumeView.as_view(template_name="resume/resume.html"),
        name="resume",
    ),
    path('admin/', admin.site.urls, name="admin-panel"),
    path("blog/", include("blog.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        ),
    ),
    path('tinymce/', include('tinymce.urls')),
    path('', include('django_prometheus.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)