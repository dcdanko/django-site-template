from django.shortcuts import render

def index(request):
	context = {
		'sitetitle':'BioBitBot',
		'navlinks':[
					],
		'projectname':'BioBitBot',
		'jumbohead':'Good Research Needs Good Analysis',
		'leadtext':'Your data. Our bioinformatics.',
		'leftsubs':[
					('About','BioBitBot provides bioinformatics analysis for microbiome research. We use bleeding edge techniques to anlyse data and provide you with detailed, easy to understand, reports. We work with your group to give you an analysis that will stand up to review')
					],
		'rightsubs':[
					('Microbiome', 'BioBitBot specializes in analyzing microbiomes.'),
					('Fast Growing', 'Our technology is backed by research. We stay up to date with nw techniques so you can focus on science.'),
					('Quick Analysis', 'Most analyses take less than 48 hours.'),
					('Open Access', 'BioBitBot is committed to Open Access science.'),
					],
		'copyright' : 'pending'



	}
	return render(request, 'generic_jumbotron.html', context)