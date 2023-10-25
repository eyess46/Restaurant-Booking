from django.db import models
from datetime import datetime

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    date_needed = models.DateField()
    email = models.EmailField()
    time = models.CharField(max_length=1000)
    number_of_people = models.IntegerField(default= 0)
    message = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)



class About(models.Model):
    
    name = models.CharField(max_length=1001)
    details = models.CharField(max_length=1001)
    


class Meal(models.Model):
    
    name = models.CharField(max_length=1001)
    details = models.CharField(max_length=1001)
    image = models.ImageField(upload_to= "meals/")
    price = models.IntegerField(default= 0)


class Gallery(models.Model):
    
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to= "gallery/")


class Review(models.Model):
    
    name = models.CharField(max_length=100) 
    state = models.CharField(max_length=500)
    image = models.ImageField(upload_to= "reviews/")
    reviews = models.CharField(max_length=500000)


class Contactform(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    subject = models.CharField(max_length= 100)
    message = models.CharField(max_length= 900)
    image = models.ImageField(upload_to= "contactforms/")