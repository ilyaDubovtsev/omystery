from django.db import models


class Quest(models.Model):
    name = models.CharField(max_length=200)
    coast = models.IntegerField()
