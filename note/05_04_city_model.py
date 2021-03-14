from cities.models import City
from django.db import models
model city
connect to admin
change and show data base

Aytike
archabeshik

in models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


# than migrations
# than
in admin.py
admin.site.register(City)

# django add s
