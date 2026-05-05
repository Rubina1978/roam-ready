from django import forms
from .models import Comment, Tip



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('tip_type', 'content',)