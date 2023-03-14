from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    age = models.IntegerField()
    description = models.TextField(max_length=500, null=True,blank=True)
    image = models.ImageField(upload_to='pictures', default="default_persons.jpg")
