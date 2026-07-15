from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Enter body', 'class': 'form-control'}),
            'publish': forms.DateTimeInput(attrs={'placeholder': 'Enter publish date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'placeholder': 'Select status', 'class': 'form-control'}),
        }