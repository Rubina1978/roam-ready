
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Destination

# Create your views here.


class DestinationsList(generic.ListView):
    queryset = Destination.objects.all()
    template_name = "destinations/home.html"
    context_object_name = "destinations"
    paginate_by = 6

#  {% comment %} adapted with help of ChatGPT {% endcomment %}


def destination_detail(request, pk):
    """Display single destination page."""

    destination = get_object_or_404(Destination, pk=pk)

    return render(request, "destinations/destination_detail.html", {"destination": destination}, )