from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title



class Odam(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField()
    gender = models.BooleanField()

    def __str__(self):
        return self.name

class Product(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.IntegerField()
    sort = models.BooleanField()
    date = models.DateTimeField()
    bio = models.TextField()

    def __str__(self):
        return self.nomi

class Car(models.Model):
    nomi = models.CharField(max_length=30)
    price = models.IntegerField()
    title = models.TextField()
    distan = models.IntegerField()
    rang = models.CharField(max_length=200)
    speed = models.IntegerField()

    def __str__(self):
        return self.nomi

class Oila(models.Model):
    ismi = models.CharField(max_length=30)
    familyasi= models.CharField(max_length=30)
    yili = models.IntegerField()
    yoshi = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.ismi


