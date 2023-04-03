from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('createBlog', views.blogPage, name="blogPost")
] 
