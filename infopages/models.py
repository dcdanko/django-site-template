from __future__ import unicode_literals

from django.db import models

class ContactInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	address = models.CharField(max_length=256)
	phone = models.CharField(max_length=256)
	email = models.EmailField()
	hours = models.CharField(max_length=256)

class FAQInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)

class FAQQuestion(models.Model):
	question = models.CharField(max_length=256)
	answer = models.TextField()

class TeamInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)

class TeamMember(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField()
	image = models.URLField()

class TechInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	content = models.TextField()

class OpenAccessInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	content = models.TextField()

class ServiceInfo(models.Model):
	heading = models.CharField(max_length=256)
	subheading = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	content = models.TextField()