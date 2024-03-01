from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    phone_number = models.IntegerField(null=True)
    address = models.TextField(null = True, max_length =200)
    