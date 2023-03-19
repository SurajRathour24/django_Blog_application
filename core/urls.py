from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("add-blog/", views.addBlog, name="addBlog"),
    path("blogdetail/<slug>", views.blogdetail, name="blogdetail"),
    path("editpost/<slug>", views.editpost, name="editpost"),
    path("DeletePost/<slug>", views.DeletePost, name="DeletePost"),
    # path("singleblog/", views.singleblog, name="singleblog1"),
    path("contact-us/", views.contact, name="contact"),
]
