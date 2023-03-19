from django.urls import path
from . import views

urlpatterns = [
    path("signin/", views.UserSignIn, name="signin"),
    path("registration/", views.UserRegistration, name="registration"),
    path("dashboard/", views.UserDashboard, name="dashboard"),
    path("profile/", views.UserProfile, name="profile"),
    path("edit-profile/", views.UpdateProfile, name="editprofile"),
    path('logout/', views.user_logout, name="logout")
]
