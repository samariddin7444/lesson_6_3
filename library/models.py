from django.db import models

class Library(models.Model):
    firth_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
