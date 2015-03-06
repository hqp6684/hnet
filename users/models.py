from django.db import models
import datetime
#Django User
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User)
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

class Employee(models.Model):
	user = models.OneToOneField(User)
	department = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class Doctor(models.Model):
	user = models.OneToOneField(Employee)
	#doctor = models.ForeignKey('Employee', verbose_name='username')
	specialty = models.CharField(max_length=100)
	office = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.specialty

class Nurse(models.Model):
	user = models.OneToOneField(Employee)

class Patient(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username


