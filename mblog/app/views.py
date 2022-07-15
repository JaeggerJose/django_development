from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    post_list = list()
    for cout, post in enumerate(posts):
        post_list.append("No.{}: ".format(str(cout))+str(post.title)+"<br>")
        post_list.append("<small>"+str(post.slug.encode('utf-8'))\
+"</small><br>"+str(post.body.encode('utf-8')+"<br><br>"))
        post_list.append("Post date is on {}".format(str(post.pub_date))+"<br><br><br>")
    return HttpResponse(post_list)