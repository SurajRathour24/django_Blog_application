from django.shortcuts import render
from .models import Post, Contact
from django.http import HttpResponseRedirect
from .forms import AddPost, EditPost
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.


#--------------------------Home View-------------------------------

def home(request):

    # send_mail(
    # 'Email Send',
    # 'Email is working',
    # 'devitech053@gmail.com',
    # ['drathour538@gmail.com'],
    # fail_silently=False,
    # )


    context ={
       'pt' : Post.objects.all(),
       'pp' : Post.objects.filter(category = 'Trending'),
       'tp' : Post.objects.filter(category = "Tech")[:1],
       'travel' : Post.objects.filter(category = "Travel"),
       'trending' : Post.objects.filter(category = "Trending"),
    } 
    
    return render(request, "core/home.html", context)




#--------------------------About View-------------------------------

def about(request):
    return render(request, "core/about.html")



#--------------------------Blog Page View-------------------------------

def blog(request):
    context = {
        'blogs' : Post.objects.all()
    }
    return render(request, "core/blog.html", context)

    


#---------------------add blog-----------------------
def addBlog(request):
    if request.method=="POST":
        print("POST added")
        fr = AddPost(data = request.POST, files = request.FILES)
        if fr.is_valid():
            fr.save()

    else:
        print("Get method work")
        fr = AddPost()
    return render(request, "core/addblog.html", {'fr':fr } )




#--------------------Edit post-----------------------

def editpost(request, slug):
    if request.method=="POST":
        pi = Post.objects.get(slug=slug)
        form = EditPost(request.POST, instance=pi, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user/dashboard/")
    else:
        pi = Post.objects.get(slug=slug)
        form = EditPost(instance=pi)
    return render(request, "core/editpost.html", {'form' : form})



#--------------------Delete post-----------------------

def DeletePost(request, slug):
    if request.method=="POST":
        pi = Post.objects.get(slug=slug)
        pi.delete()
        return HttpResponseRedirect('/user/dashboard/')


#-------------------------------Contact us ----------------------------------

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = Contact(name=name, email=email, message=message)
        data.save()
        email_subject = "Enquiry Form"
        email_message = request.POST.get('message')
        email_message = request.POST.get('message')
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
        messages.info(request, "Form submited")
        return HttpResponseRedirect('/contact-us/')
    return render(request, "core/contact.html")



#--------------Single blog-------------------------

def blogdetail(request, slug):
    context = {
        'post' : Post.objects.get(slug=slug)
    }
    return render(request, "core/singleblog.html", context)


