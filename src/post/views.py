
from django.shortcuts import render

from .models import Post
from marketing.models import Signup

def index(request):
	featured = Post.objects.filter(featured=True)
	latest = Post.objects.order_by('-timestamp')[0:3]

	if request.method == "POST":
		email = request.POST["email"]
		new_signup = Signup()
		new_signup.email = email
		new_signup.save()

	context ={
		'object_list': featured,
		'latest':latest
	}
	return render(request, 'index.html', context)

def blog(request):
	post_list = Post.objects.all()
	most_recent = Post.objects.order_by('-timestamp')[0:3]

	context ={
		"post_list": post_list,
		"most_recent": most_recent
	}
	return render(request, 'blog.html', context)

def post(request):
	return render(request, 'post.html', {})