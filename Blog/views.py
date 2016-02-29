from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from Blog.models import MyPost

def articles(request):
    posts = MyPost.objects.all()
    t = loader.get_template('post.html')
    c = Context({'posts': posts })
    return HttpResponse(t.render(c))