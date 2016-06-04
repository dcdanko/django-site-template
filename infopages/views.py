from django.http import Http404
from django.shortcuts import render
from .models import * 


def tech(request):
	info = TechInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]

	context = {
		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'content':info.content,
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)

def openAccess(request):
	info = OpenAccessInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]

	context = {
		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'content':info.content,
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)

def team(request):
	info = TeamInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]

	items = TeamMember.objects.all()
	pairs = [items]
	print(pairs)
	context = {
		'itempairs':pairs,

		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'copyright':'Pending',

	}
	return render(request,'portfolio-2-col.html',context)

def contact(request):
	info = ContactInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]
	context = {
		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'copyright':'Pending',
		'phone':info.phone,
		'email':info.email,
		'hours':info.hours,
		'address':info.address.split('\n'),
	}
	return render(request,'contact.html',context)

def faq(request):
	info = FAQInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]
	questions = FAQQuestion.objects.all()
	context = {
		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'questions':questions,
		'copyright':'Pending',
	}
	return render(request,'faq.html',context)

def service(request):
	info = ServiceInfo.objects.all()
	if len(info) != 1:
		raise Http404('Information not found.')
	info = info[0]

	context = {
		'heading':info.heading,
		'subheading':info.subheading,
		'title':info.title,
		'content':info.content,
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)