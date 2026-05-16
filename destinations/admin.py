from django.contrib import admin
from .models import Destination, Tip, Comment

# Register your models here.
admin.site.register(Destination)
admin.site.register(Tip)
admin.site.register(Comment)
