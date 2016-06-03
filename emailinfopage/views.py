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



