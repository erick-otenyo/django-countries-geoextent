from django.db import models

from django_countries.fields import CountryField


class Home(models.Model):
    country = CountryField()

    def __str__(self):
        if hasattr(self.country, "geo_extent") and self.country.geo_extent:
            return f"{self.country.name}  - {str(self.country.geo_extent)}"
        return "No GeoExtent"
