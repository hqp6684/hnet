from django.db import models

#Django User
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	dOB = models.DateField()
	sSN = models.CharField(max_length=11)
	phoneNumber = models.CharField(max_length=10)
	streetAddress = models.CharField(max_length=100)
	city = models.CharField(max_length=40)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=5)

class Employee(models.Model):
	user = models.OneToOneField(User)
	department = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class Doctor(models.Model):
	user = models.OneToOneField(Employee)
	specialty = models.CharField(max_length=100)

class Nurse(models.Model):
	user = models.OneToOneField(Employee)

class Patient(models.Model):
	user = models.OneToOneField(User)


