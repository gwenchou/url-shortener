from http import HTTPStatus
from django.views import View
from django.http import JsonResponse, HttpResponseRedirect
from url_shortener.models import Shortened_Url


def redirect_from_alias(self, alias):
    shortened_url = Shortened_Url.objects.get(alias=alias)

    return HttpResponseRedirect(shortened_url.origin_url)


class UrlShortener(View):
    def post(self, request):
        shortened_url = Shortened_Url.objects.create(
            origin_url=request.POST['origin_url']
        )

        return JsonResponse({
            'alias': shortened_url.alias,
            'origin_url': shortened_url.origin_url
        }, status=HTTPStatus.CREATED)

    def get(self, request, alias):
        shortened_url = Shortened_Url.objects.get(alias=alias)
        
        return JsonResponse({
            'alias': shortened_url.alias,
            'origin_url': shortened_url.origin_url
        }, status=HTTPStatus.OK)
