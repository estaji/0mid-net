from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from resume.views import ResumeView


urlpatterns = [
    path(
        "",
        ResumeView.as_view(template_name="resume/resume.html"),
        name="resume",
    ),
    path('admin/', admin.site.urls, name="admin-panel"),
    path("blog/", include("blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)