from http import HTTPStatus
from django.test import TestCase, Client

# Create your tests here.
class UrlShortenerTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_shortened_url(self):
        origin_url = 'https://google.com'
        http_client = Client()
        response = http_client.post('/shortened_urls/', {'origin_url': origin_url})
        print(response.content)
        response_content = response.json()

        # self.assertEqual(response_content['origin_url'], origin_url)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(response_content['origin_url'], origin_url)
