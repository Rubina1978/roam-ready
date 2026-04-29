from django.shortcuts import render

from django.views import generic
from .models import Destination

# Create your views here.


class DestinationsList(generic.ListView):
    queryset = Destination.objects.all()
    template_name = "destinations/home.html"
    context_object_name = "destinations"
    paginate_by = 6