from django.urls import path

from url_shortener.views import UrlShortener

app_name = 'url_shortener'
urlpatterns = [
    path('', UrlShortener.as_view(), name='create'),
    path('<slug:alias>/', UrlShortener.as_view()),
]
