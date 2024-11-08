from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration"),
    path("logout/", views.logout, name="logout"),
    path("profile_change/", views.profile_change, name="profile_change"),
]