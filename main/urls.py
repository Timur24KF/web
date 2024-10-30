from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:id>", views.post, name="post"),
]
