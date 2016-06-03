from django.shortcuts import render, redirect
from .models import InterestedEmail, InterestedEmailForm

def addInterestedEmail(request):
	if request.method == 'POST':
		form = InterestedEmailForm(request.POST)
		if form.is_valid():
			query = InterestedEmail(iemail=form.cleaned_data['iemail'])
			query.save()
			print('Saved email!')
	return redirect('/')



def index(request):

	context = {	
		'navbartitle'			:"BioBitBot",
		'sitetitle'				:"BioBitBot",		
		'carouselimages'		:""	,		
		'welcomemsg'			:"Your Data. Our Bioinformatics."	,		
		'paneltitleone'			:"The Microbiota",		
		'panelbodyone'			:'BioBitBot specializes in analyzing microbiomes from whole genome sequencing. This produces the most detailed portraits of microbiomes currently possible.'	,		
		'panelbuttonone'		:""	,		
		'paneltitletwo'			:"Start To Finish"	,		
		'panelbodytwo'			:'We handle your data all the way from quality control until it\'s uploaded to a public database. We work with you every step of the way to make sure your needs are met.'	,		
		'panelbuttontwo'		:""	,		
		'paneltitlethree'		:"Custom Analysis"	,		
		'panelbodythree'		:'We tailor our analysis to fit your research. We can analyse many sources of data including microarrays, host sequence data, and flow cytometry.'	,		
		'panelbuttonthree'		:""	,	
		'calltoactionbutton'	:""	,		
		'calltoaction'			:""	,		

	}
	return render(request, 'index.html', context)


def tech(request):
	context = {
		'heading':'The Technology We Use',
		'subheading':'Cutting Edge.',
		'title':'Technology',
		'content':'Coming Soon!',
		'navbartitle'			:"BioBitBot",
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)

def openAccess(request):
	context = {
		'heading':'Our Commitment to Open Access.',
		'subheading':'Enabling Science',
		'title':'Open Access',
		'content':'Coming Soon!',
		'navbartitle'			:"BioBitBot",
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)

def team(request):
	items = [{'title':'David','content':'PhD Candidate','image':'https://cdn0.iconfinder.com/data/icons/huge-basic-icons-part-2/512/Man.png'}]
	pairs = [items]
	print(pairs)
	context = {
		'itempairs':pairs,

		'heading':'Our Team.',
		'subheading':'Enabling Science',
		'title':'The Team',
		'navbartitle':"BioBitBot",
		'copyright':'Pending',

	}
	return render(request,'portfolio-2-col.html',context)

def contact(request):
	context = {
		'heading':'Contact us.',
		'subheading':'Anytime.',
		'title':'Contact Info',
		'navbartitle':"BioBitBot",
		'copyright':'Pending',
		'phone':'07521 788173',
		'email':'dcdanko@gmail.com',
		'hours':'Data never sleeps!',
		'address':['34 Henley St','Oxford, OX4 1ES U.K.']
	}
	return render(request,'contact.html',context)

def faq(request):
	questions = [{'question':'What is BioBitBot?','answer':'A great way to analyze your data!'}]
	context = {
		'heading':'Frequently Asked Questions.',
		'subheading':'',
		'title':'FAQ',
		'questions':questions,
		'copyright':'Pending',
		'navbartitle':"BioBitBot",
	}
	return render(request,'faq.html',context)

def service(request):
	context = {
		'heading':'The Services We Provide',
		'subheading':'Start to Finish.',
		'title':'Service',
		'content':'Coming Soon!',
		'navbartitle'			:"BioBitBot",
		'copyright':'Pending',

	}
	return render(request,'full-width.html',context)
