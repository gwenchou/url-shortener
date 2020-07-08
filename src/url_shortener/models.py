import random
import string
from django.db import models
from django.forms import ModelForm


class ShortenedUrlAliasField(models.SlugField):
    def pre_save(self, model_instance, add):
        if add:
            model_instance.alias = self.get_shortened_url_alias_slug()

        return model_instance.alias

    def get_shortened_url_alias_slug(self):
        alias = ''.join(random.choices(string.ascii_letters + string.digits + '_' + '-', k=6))

        if Shortened_Url.objects.filter(alias=alias).exists():
            return self.get_shortened_url_alias_slug()

        return alias

class Shortened_Url(models.Model):
    alias = ShortenedUrlAliasField(max_length=8, unique=True)
    origin_url = models.URLField(max_length=2048)


class ShortenedUrlForm(ModelForm):
    class Meta:
        model = Shortened_Url
        fields = ['origin_url']
