import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from froala_editor.fields import FroalaField
# Create your models here.





STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY_CHOICES = (
    ('Uncategorized', 'Uncategorized'),
    ('Travel', 'Travel'),
    ('Food', 'Food'),
    ('Tech', 'Tech'),
    ('Jobs', 'Jobs'),
    ('business', 'business'),
    ('sports', 'sports'),
    ('Trending', 'Trending'),
    ('Popular', 'Popular'),
    ('Inspiration', 'Inspiration'),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300 , unique=True, default=uuid.uuid1)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    # description = RichTextField(blank=True, null=True)
    description = FroalaField()
    created_on = models.DateTimeField(auto_now=True)
    feature_image = models.ImageField(upload_to='featured_image/%Y/%m/%d/' ,null=True, blank=True)
    blog_image = models.ImageField(null=True, blank=True, upload_to="blogimages/")
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(choices=CATEGORY_CHOICES, default="Uncategorized", max_length=50)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    message = models.TextField()