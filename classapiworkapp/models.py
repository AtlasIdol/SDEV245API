from django.db import models

# Create your models here.
class Student(models.Model):
    cnumber = models.CharField(primary_key=True, max_length=10)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    major = models.CharField(max_length=25)
    dob = models.DateField()
    gpa = models.FloatField()

    def __str__(self):
        return self.lastname