from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Employee, Doctor, Nurse, Patient, UserProfile

# Register your models here.


admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Doctor)
admin.site.register(UserProfile)