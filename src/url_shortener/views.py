from http import HTTPStatus
from django.views import View
from django.http import JsonResponse
from url_shortener.models import Shortened_Url


class UrlShortener(View):
    def post(self, request):
        shortened_url = Shortened_Url.objects.create(
            origin_url=request.POST['origin_url']
        )

        return JsonResponse({
            'alias': shortened_url.alias,
            'origin_url': shortened_url.origin_url
        }, status=HTTPStatus.CREATED)

    def get(self, request, slug):
        shortened_url = Shortened_Url.objects.get(alias=slug)
        
        return JsonResponse({
            'alias': shortened_url.alias,
            'origin_url': shortened_url.origin_url
        }, status=HTTPStatus.OK)
