from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class InterestedEmail(models.Model):
	iemail = models.EmailField()


class InterestedEmailForm(ModelForm):
    class Meta:
        model = InterestedEmail
        fields = ('iemail',)