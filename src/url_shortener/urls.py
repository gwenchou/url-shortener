from django.urls import path

from url_shortener.views import UrlShortenerApi

app_name = 'url_shortener'
urlpatterns = [
    path('', UrlShortenerApi.as_view(), name='create'),
    path('<slug:alias>/', UrlShortenerApi.as_view()),
]
