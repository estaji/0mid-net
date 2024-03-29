from django.urls import path

from .views import FreshResultView, HomeView, HttpView, PingView, ResultView

app_name = "scan"

urlpatterns = [
    path("", HomeView.as_view(), name="scan-home"),
    path("result/<uuid:uuid>", ResultView.as_view(), name="result"),
    path(
        "result/<uuid:uuid>/freshresult",
        FreshResultView.as_view(),
        name="scan-fresh-result",
    ),
    path("api/ping/", PingView.as_view(), name="api-ping"),
    path("api/http/", HttpView.as_view(), name="api-http"),
]
