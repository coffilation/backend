from django.db import models
from django.db.models.constraints import UniqueConstraint


class Place(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    osm_id = models.BigIntegerField()
    osm_type = models.CharField(max_length=255)
    display_name = models.CharField(max_length=2000)
    category = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.JSONField()

    class Meta:
        constraints = [UniqueConstraint(
            fields=['osm_id', 'osm_type', 'category'],
            name='place_osm_identificators'
        )]

    def __str__(self):
        return self.display_name
