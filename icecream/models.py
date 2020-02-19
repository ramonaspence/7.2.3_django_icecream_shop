from django.db import models
from django.urls import reverse

class Icecream(models.Model):
    flavor = models.CharField(max_length = 255)
    base = models.CharField(max_length = 255, choices=[('chocalate', 'chocolate'), ('vanilla', 'vanilla')])
    available = models.CharField(max_length = 255, choices = [('seasonal', 'seasonal'), ('weekly', 'weekly'), ('daily', 'daily')])
    featured = models.BooleanField()
    date_churned = models.DateField()


    def __str__(self):
        return self.flavor


# Create your models here.
