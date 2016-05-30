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
		'sitetitle':'BioBitBot',
		'navlinks':[
					],
		'projectname':'BioBitBot',
		'leadtext':'Good research needs good analysis',
		'jumbohead':['Your Data.','Our Bioinformatics.'],
		'sections':[
						[
							('About','BioBitBot provides bioinformatics analysis for microbiome research. We use bleeding edge techniques to anlyse data and provide you with detailed, easy to understand, reports. We work with your group to give you an analysis that will stand up to review')
						],
						[
							('Microbiome', 'BioBitBot specializes in analyzing microbiomes.'),
							('Fast Growing', 'Our technology is backed by research. We stay up to date with nw techniques so you can focus on science.'),
							('Quick Analysis', 'Most analyses take less than 48 hours.'),
							('Open Access', 'BioBitBot is committed to Open Access science.'),
						],
					],
		'copyright' : 'pending'



	}
	return render(request, 'generic_jumbotron.html', context)