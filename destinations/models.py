from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
TIP_TYPES = [
    ('general', 'General'),
    ('food', 'Food'),
    ('views', 'Views'),
    ('attractions', 'Attractions'),
    ('sightseeing', 'Sightseeing'),
    ('outdoors', 'Outdoors'),
    
]

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
    category = models.CharField(max_length=50)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on', 'country', 'category']

    def __str__(self):
        return self.name
    

class Tip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="tips")
    tip_type = models.CharField(max_length=100, choices=TIP_TYPES)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tips", null=True, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['tip_type', 'destination']

    def __str__(self):
        return f"{self.tip_type} - {self.destination.name}"
    

class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.destination.name}"