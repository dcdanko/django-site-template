from django.http import Http404
from django.shortcuts import render
from .models import *

def index(request):
	info = HomeInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]
	blurbs = Blurb.objects.all()
	triblurbs = makeTriples(blurbs)
	banner = Banner.objects.all()[0]

	context = {		
		'banner'				: banner,		
		'welcomemsg'			: info.tagline,	
		'blurbs'				: triblurbs,
		'example_email'			: info.example_email,
		'email_button'			: info.email_button,
		'copyright'				: 'Pending',	
	}
	return render(request, 'index.html', context)

def makeTriples(l):
	if len(l) <= 3:
		return [l]

	l1 = l[::3]
	l2 = l[1::3]
	l3 = l[2::3]

	out = []
	for i in range(len(l3)):
		out.append( [l1[i],l2[i],l3[i]])

	if len(l1) > len(l3):
		out.append([l1[-1]])
	if len(l2) > len(l3):
		out[-1].append(l2[-1])
	return out