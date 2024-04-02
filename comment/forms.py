from django import forms
from .models import Comment
class Review(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','text',]
        labels={
            'text':'Write your Review',
            'name':'Name'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}) 
        }