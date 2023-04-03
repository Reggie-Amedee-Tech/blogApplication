from django.shortcuts import render
from .models import Blog

def homepage (request):
    data=Blog.objects.all()
    context={"data": data}
    return render(request, "homepage.html", context)

def blogPage (request):
    data=Blog.objects.all()
    if request.method == "POST":
        title=request.POST.get(title)
        content=request.POST.get(content)

    context={"data": data}
    
    return render(request, "blogpostForm.html", context)
