from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status = (
    (0, "Draft"),
    (1, "Publish")
)

class Blog(models.Model):
    slug=models.SlugField(max_length=200, unique=True, null=True)
    title=models.CharField(max_length=200, unique=True)
    author=models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content=models.TextField()
    created_on=models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=status, default=0)
    

class Meta: 
    ordering = ['-created_on']

def __str__(self):
    return self.name



