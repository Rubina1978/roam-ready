from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
    category = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ['country', 'category']

    def __str__(self):
        return self.name
    

class Tip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    tip_type = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['tip_type', 'destination']

    def __str__(self):
        return f"{self.tip_type} - {self.destination.name}"
    

class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.destination.name}"