from django.urls import path

from url_shortener.views import UrlShortener

urlpatterns = [
    path('', UrlShortener.as_view()),
    path('<slug:alias>/', UrlShortener.as_view()),
]
