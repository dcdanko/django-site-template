from django.test import TestCase

class AddInterestedEmailTests(TestCase):

	def add_simple_email(self):
		response = self.client.post('/postemail/', {'iemail':'test@email.com'})
