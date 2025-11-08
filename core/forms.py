# core/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "What's happening?",
                "class": "form-control",
            }),
            "image": forms.ClearableFileInput(attrs={"class": "form-control mt-2"})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {"text": forms.TextInput(attrs={"placeholder": "Add a comment...", "class": "form-control d-inline-block", "style": "width:65%"})}
# core/forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content", "image"]
        widgets = {
            "content": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "What's happening?",
                "class": "form-control",
            }),
            "image": forms.ClearableFileInput(attrs={"class": "form-control mt-2"})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {"text": forms.TextInput(attrs={"placeholder": "Add a comment...", "class": "form-control d-inline-block", "style": "width:65%"})}
