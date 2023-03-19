from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import UserRegistrationForm
from core.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import EditProfile

# Create your views here.



####-------------------------------------------user registration------------
 
def UserRegistration(request):
 
    if request.user.is_authenticated:
        return redirect('/user/dashboard')
     
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
 
        if form.is_valid():
            messages.info(request, "Welcome {} Account has been created successfully !!".format(request.user.username))
            form.save()
            return HttpResponseRedirect('/user/signin/')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/user/dashboard')
         
        else:
            return render(request,'authsys/register.html',{'form':form})
     
    else:
        form = UserRegistrationForm()
        return render(request,'authsys/register.html',{'form':form})
 


#--------------------------------User Signin-------------------------------------

def UserSignIn(request):
    if request.user.is_authenticated:
        return redirect('/user/dashboard')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            messages.info(request, "Welcome {} You are logged in successfully !!".format(request.user.username))
            return redirect('/user/dashboard')
        else:
            form = AuthenticationForm()
            return render(request,'authsys/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'authsys/signin.html', {'form':form})


#----------------------------user dashboard---------------------

def UserDashboard(request):
    # messages.info(request, "Welcome {} ".format(request.user.username))
    if request.user.is_staff: 
        author = request.user.id
        print(author)
        post = Post.objects.filter(author = author)[:3]
        print(post)
        return render(request, "authsys/dashboard.html", {'ps': post})
    else:
        return HttpResponseRedirect('/')


#-----------------------UserProfile-----------------

def UserProfile(request):
    return render(request, "authsys/profile.html")




#----------------edit user profile 
def UpdateProfile(request):
    if request.user=="POST":
        fm = EditProfile(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/user/dashboard/')
    else:
        fm = EditProfile(instance=request.user)
    
    return render(request, "authsys/editprofile.html",{'fm':fm})



#-------------------user logout-------------------

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/signin/')