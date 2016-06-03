from django.http import Http404
from django.shortcuts import render
from .models import *

def index(request):
	info = HomeInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]
	blurbs = Blurb.objects.all()
	triblurbs = [blurbs]
	banners = Banner.objects.all()

	context = {	
		'navbartitle'			:"BioBitBot",
		'sitetitle'				:"BioBitBot",		
		'banners'				: banners,		
		'welcomemsg'			: info.tagline,	
		'blurbs'				: triblurbs,
		'example_email'			: info.example_email,
		'email_button'			: info.email_button,
		'copyright'				: 'Pending',	
	}
	return render(request, 'index.html', context)