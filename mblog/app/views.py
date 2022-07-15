from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request , 'index.html', locals())