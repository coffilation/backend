from django.db import models
from apps.places.models import Place
from django.contrib.auth.models import User


class Compilation(models.Model):
    is_private = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    primary_color = models.CharField(max_length=7, null=True, blank=True)
    secondary_color = models.CharField(max_length=7, null=True, blank=True)
    places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return self.name
