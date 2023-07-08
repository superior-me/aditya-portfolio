from django.urls import path
from .import views

urlpatterns = [
    path("", views.index),
    path("portfolio/", views.index),
    path("contact/", views.contact),
    path("projects/", views.projects),
    path("resume/", views.resume),  
]
