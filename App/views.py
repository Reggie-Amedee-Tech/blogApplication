from django.shortcuts import render
from .models import Blog

def blogPosts (request):
    data=Blog.objects.all()
    context={"data": data}
    return render(request, "blogPosts.html", context)

def blogpostpage(request,id):
    data=Blog.objects.filter(id=id)
    print(data)
    context={"data": data}
    return render(request, "blogPostContent.html", context)

def homepage2(request):
    data=Blog.objects.all()
    context={"data": data}
    return render(request, "homepage2.html", context)

def aboutpage(request):
        return render(request, "about.html")
