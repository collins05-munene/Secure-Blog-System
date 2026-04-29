from django.forms import ModelForm

from .models import Post

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']
