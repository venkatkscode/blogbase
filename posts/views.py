from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .models import Post 


# Create your views here.

def posts_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	context = {
		"title":instance.title,
		"instance": instance
	}
	return render(request,"posts_detail.html",context)

def posts_list(request):
	queryset = Post.objects.all()
	
	
	context = {
		"object_list": queryset,
	}
	return render(request,"index.html",context)


