"""
Definition of models.
"""

from django.db import models

class Site(models.Model):
    name = models.CharField("site",max_length = 200)

class SiteDetails(models.Model):
    date = models.DateField('date')
    a_value = models.FloatField('A Value')
    b_value = models.FloatField('B Value')
    site = models.ForeignKey(Site)

