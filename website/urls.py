from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('gallery.html', views.gallery, name="gallery"),
    path('404.html', views.error, name="error"),
]