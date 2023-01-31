from django.shortcuts import render
from django.http import HttpResponse

#importing Tables in DB
from .models import Post
# Create your views here.

## we are trying to pass dummy data to templates.
'''posts=[
    {
        'author':'Amar',
        'title': 'Blog Post',
        'content': 'First post',
        'date_posted':'January 01, 2023'
    },
    {
        'author':'Harika',
        'title': 'Blog Post 2',
        'content': 'First post',
        'date_posted':'January 01, 2023'
    }
]'''
## we post this above data passing it as argument with our data

def home(request):
    ##Our data
    context={
        'posts': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>') ---if we want to pass html code.
    ##if we want to render html file we have to create in temoplates/<app_name> the we use render function 
    ##which is already in django.shortcuts
    return render(request,'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title':'About'})