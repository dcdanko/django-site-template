from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blogIndex(request):
	blogposts = BlogPost.objects.order_by('-pub_date')
	context = {
		'heading':'The Blog',
		'subheading':'',
		'title':'Blog',
		'copyright':'Pending',
		'blogposts':blogposts,
	}
	return render(request,'blog-home-2.html',context)

def blogDetail(request,postid):
	post = get_object_or_404(BlogPost, pk=postid)
	context = {
		'post' : post,
		'copyright':'Pending',
		}
	return render(request,'blog-post.html',context)