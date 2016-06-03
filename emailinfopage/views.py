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





