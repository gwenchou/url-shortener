import json
from http import HTTPStatus
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from url_shortener.models import Shortened_Url, ShortenedUrlForm


def home(request):
    return render(request, 'home.html')


def shortened_url_detail(request, alias):
    shortened_url = Shortened_Url.objects.get(alias=alias)

    return render(
        request,
        'shortened_url_detail.html',
        {'alias': alias, 'origin_url': shortened_url.origin_url}
    )


def redirect_from_alias(request, alias):
    shortened_url = Shortened_Url.objects.get(alias=alias)

    return HttpResponseRedirect(shortened_url.origin_url)


class UrlShortenerApi(View):
    def post(self, request):
        shortened_url_form = ShortenedUrlForm({
            'origin_url':json.loads(request.body).get('origin_url')
        })

        if not shortened_url_form.is_valid():
            return JsonResponse(shortened_url_form.errors)

        shortened_url = shortened_url_form.save()

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
