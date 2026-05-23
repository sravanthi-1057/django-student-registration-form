from django.db import models

# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    rollno = models.CharField(max_length=20)
    address = models.TextField()
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    skills = models.CharField(max_length=100)
    mode = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')
    about = models.TextField()