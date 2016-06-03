from __future__ import unicode_literals

from django.db import models


class BlogPost(models.Model):
	title = models.CharField(max_length=256)
	author = models.CharField(max_length=256)
	pub_date =  models.DateTimeField(auto_now=True)
	content = models.TextField()
	image = models.CharField(max_length=256)