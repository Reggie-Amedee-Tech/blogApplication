from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views

urlpatterns = [
    path('blogPosts', views.blogPosts, name="homepage"),
    path('blogPost/<id>', views.blogpostpage, name="blogPostContent"),
    path('', views.homepage2, name="homepage2"),
    path('about', views.aboutpage, name="about")
] 
