from django.db import models
from apps.places.models import Place
from django.contrib.auth.models import User


class Compilation(models.Model):
    is_private = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1023)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    places = models.ManyToManyField(Place)
