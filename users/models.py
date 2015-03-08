from django.db import models
import datetime
#Django User
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	dOB = models.DateField(null=True)
	sSN = models.CharField(max_length=11,default='000-00-0000',blank=True)
	phoneNumber = models.CharField(max_length=15,default='xxx-xxx-xxxx',null=True)
	streetAddress = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=30,blank=True)
	state = models.CharField(max_length=2,blank=True)
	zipcode = models.CharField(max_length=5,default='xxxxx',blank=True)
	email = models.EmailField(max_length=75, blank=True)

	def __str__(self):
		return self.user.username
	@classmethod
	def create(u, username):
		userprofile = u(user=username)
		return userprofile

	'''return url for an object'''
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		#return "/users/%i/" % self.user.id
		return reverse('userprofile-detail', kwargs={'pk':self.user.id})
	
	def get_field_values(self):
		return [field.value_to_string(self) for field in UserProfile._meta.fields]

class Employee(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	department = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class Doctor(models.Model):
	user = models.OneToOneField(Employee,primary_key=True)
	#doctor = models.ForeignKey('Employee', verbose_name='username')
	specialty = models.CharField(max_length=100)
	office = models.CharField(max_length=50, blank=True)
	'''
	patient  oneToMany Patient
	
	'''

	def __str__(self):
		return self.specialty

class Nurse(models.Model,):
	user = models.OneToOneField(Employee,primary_key=True)

class Patient(models.Model):
	user = models.OneToOneField(User,primary_key=True)
	@classmethod
	def create(p, username):
		patient = p(user=username)
		return patient

	def __str__(self):
		return self.user.username


