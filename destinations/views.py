
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Destination
from .forms import CommentForm

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
    comments = destination.comments.all().order_by("-created_on")
    comment_count = destination.comments.filter(approved=True).count()

#{% comment %}handling the comments{ % endcomment %}
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.destination = destination
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your comment, your comment is awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request, 
        "destinations/destination_detail.html", 
        {"destination": destination,
         "comments":comments,
         "comment_count": comment_count,
         "comment_form": comment_form} 
         )