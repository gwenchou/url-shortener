import json
from http import HTTPStatus
from django.test import TestCase, Client
from url_shortener.models import Shortened_Url


class UrlShortenerTestCase(TestCase):
    def setUp(self):
        self.http_client = Client()

    def test_redirect_from_alias(self):
        origin_url = 'https://google.com'
        shortened_url = Shortened_Url.objects.create(
            origin_url=origin_url,
        )

        response = self.http_client.get('/{}/'.format(shortened_url.alias), follow=True)
        self.assertEqual(response.redirect_chain, [(origin_url, 302)])

    def test_create_shortened_url(self):
        origin_url = 'https://google.com'
        response = self.http_client.post(
            '/shortened_urls/',
            json.dumps({'origin_url': origin_url}),
            content_type="application/json"
        )
        response_content = response.json()

        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response_content['origin_url'], origin_url)

    def test_retrieve_shortened_url(self):
        origin_url = 'https://google.com'
        shortened_url = Shortened_Url.objects.create(
            origin_url=origin_url,
        )

        response = self.http_client.get('/shortened_urls/{}/'.format(shortened_url.alias))
        response_content = response.json()
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response_content['origin_url'], origin_url)
