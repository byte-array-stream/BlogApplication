from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    image = models.ImageField()
    url = models.URLField(blank = True)
