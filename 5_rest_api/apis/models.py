from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField()

class Classroom(models.Model):
    year = models.IntegerField()
    room_number = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)