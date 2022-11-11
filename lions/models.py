from django.db import models


class Lion(models.Model):
    name = models.CharField(max_length=200)
    body_count = models.FloatField()
    fig_url = models.CharField(max_length=2083)



