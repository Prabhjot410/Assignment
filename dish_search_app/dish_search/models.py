from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()
    latitude = models.FloatField()
    details = models.TextField()

    def __str__(self):
        return self.name
