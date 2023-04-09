from django.shortcuts import render
from .models import Blog

def homepage (request):
    data=Blog.objects.all()
    context={"data": data}
    return render(request, "homepage.html", context)

def blogpostpage(request,id):
    data=Blog.objects.filter(id=id)
    print(data)
    context={"data": data}
    return render(request, "blogPostContent.html", context)
