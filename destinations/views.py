
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Destination, Comment, Tip
from .forms import CommentForm, TipForm

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
    tips = destination.tips.all().order_by("tip_type")


# handling the comments
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
    
# tip handling
    if request.method == "POST":
        tip_form = TipForm(request.POST)
        if tip_form.is_valid():
            tips = tip_form.save(commit=False)
            tips.user = request.user
            tips.destination = destination
            tips.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Tip submitted and awaiting approval'
            )
   
    tip_form = TipForm()

    return render(
        request, 
        "destinations/destination_detail.html", 
        {"destination": destination,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         "tip_form": tip_form
         },
         
    )

# editing comments and tips


def comment_edit(request, destination_id, comment_id):
    """View for editing comments"""
    """built with help of ChatGPT"""

    if request.method == "POST":

        destination = get_object_or_404(Destination,  pk=destination_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.destination = destination
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment was updated successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Sorry an error occured, please try again')

    return HttpResponseRedirect(reverse('destination_detail', args=[destination_id]))


def tip_edit(request, destination_id, tip_id):

    """View for editing tips"""

    if request.method == "POST":
        destination = get_object_or_404(Destination, pk=destination_id)
        tip = get_object_or_404(Tip, pk=tip_id)
        tip_form = TipForm(data=request.POST, instance=tip)
        if tip_form.is_valid() and tip.user == request.user:
            tip = tip_form.save(commit=False)
            tip.destination = destination
            tip.approved = False
            tip.save()
            messages.add_message(request, messages.SUCCESS, 'Your tip was successfully updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Sorry an error occured, please try again')
            
    return HttpResponseRedirect(reverse('destination_detail', args=[destination_id]))

# deleting comments and tips


def comment_delete(request, destination_id, comment_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    comment = get_object_or_404(Comment, pk=comment_id, destination=destination)
    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comment!')

    return HttpResponseRedirect(reverse('destination_detail', args=[destination.id]))
        

def tip_delete(request, destination_id, tip_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    tip = get_object_or_404(Tip, pk=tip_id)
    if tip.user == request.user:
        tip.delete()
        messages.add_message(request, messages.SUCCESS, 'Your tip has been deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your tips!')

    return HttpResponseRedirect(reverse('destination_detail', args=[destination.id]))