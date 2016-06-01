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
							('About','BioBitBot provides custom bioinformatics analysis for microbiome research. We use bleeding edge techniques to analyse data and provide you with detailed, easy to understand, reports. We work with your group to give you an analysis that will stand up to review. If you\'re interested in how BioBitBot can help you, sign up for more information.')
						],
						[
							('Microbiomes', 'BioBitBot specializes in analyzing microbiomes from whole genome sequencing. This produces the most detailed portraits of microbiomes currently possible.'),
							('Start to Finish', 'We handle your data all the way from quality control until it\'s uploaded to a public database. We work with you every step of the way to make sure your needs are met.'),
							('Custom Analysis','We tailor our analysis to fit your research. We can analyse many sources of data including microarrays, host sequence data, and flow cytometry.'),
							('Fast Growing', 'Our technology is backed by research. We stay up to date with new techniques so you can focus on science. All our techniques are transparent and easily included in publication.'),
							('Quick Analysis', 'Most analyses take less than a week from start to finish. We\'ll work to match your schedule.'),
							('Open Access', 'BioBitBot is committed to Open Access science. Our tool stack is listed publically. We help our clients make their data publically available.'),
						],
					],
		'copyright' : 'pending'



	}
	return render(request, 'generic_jumbotron.html', context)