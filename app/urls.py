from django.urls import path
from app import views

urlpatterns = [
    path("echo/", views.echo_page),
]
