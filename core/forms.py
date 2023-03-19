from django import forms
from .models import Post


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug' ,'description', 'author' ,'status', 'category', 'blog_image', 'feature_image']



class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description', 'author' ,'status', 'category', 'blog_image', 'feature_image']