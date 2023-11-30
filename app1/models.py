from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Courses(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField(null=True)


class StudentDetails(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    address=models.CharField(max_length=255)
    doj=models.DateField()

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255)
    img=models.ImageField(null=True)
