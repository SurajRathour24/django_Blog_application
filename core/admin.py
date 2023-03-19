from django.contrib import admin
from .models import Post, Contact
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug' ,'author', 'updated_on','created_on', 'blog_image', 'status', 'category']
    list_filter = ("status",)
    search_fields = ['title', 'category']
    # prepopulated_fields = {'slug': ('title',)}


@admin.register(Contact)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']