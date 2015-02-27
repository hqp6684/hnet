from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Employee, Doctor, Nurse

# Register your models here.


admin.site.register(Employee)