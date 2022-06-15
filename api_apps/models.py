from django.db import models

# Create your models here.
class student(models.Model):
    objects = None
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)


class Teacher(models.Model):
    objects = None
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
s=student(1,'shital','kadam') #this is object of student class and that's why we store a value on database
s.save()  # this line to save the info in database

t=Teacher(1,'shital','kadam','shitalkadam765@gmail.com')
t.save()