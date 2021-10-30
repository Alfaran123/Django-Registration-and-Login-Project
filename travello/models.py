from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()


class Employee(models.Model):
    emp_first_name=models.CharField(max_length=200)
    emp_salary=models.IntegerField()
    emp_last_name=models.CharField(max_length=200)