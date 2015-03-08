from django.db import models

from users.models import Patient
# Create your models here.
'''
class MediacalInformation(models.Model):
	user = models.OneToOneField(Patient, primary_key=True)
	allergies = models.CharField(max_length=100, blank=True)
	medication = models.CharField(max_length=100, blank=True)
	#history = models.CharField(max_length=100, blank=True)
'''
class Medicalinfo(models.Model):
	user = models.OneToOneField(Patient, primary_key=True)
	allergies = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.user.user.username

	@classmethod
	def create(m, username):
		medicalinfo = m(user=username)
		return medicalinfo

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		#return "/users/%i/" % self.user.id
		return reverse('patient-medicalinfo', kwargs={'pk':self.user.user.id})
	
