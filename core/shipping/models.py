from django.db import models

# Create your models here.
    
class Client(models.Model):
    name = models.CharField(max_length=200, blank=True)
    adress = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    rfc = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    description = models.CharField(max_length=255)
    variety = models.CharField(max_length=100)
    packaging = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    box = models.IntegerField()

    def __str__(self):
        return self.description
    
class Driver(models.Model):
    name = models.CharField(max_length=255)
    license = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=255)
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.description
    
class Truck(models.Model):
    made = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    plate = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Container(models.Model):
    number = models.CharField(max_length=6)
    plate = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Custom(models.Model):
    destination =  models.CharField(max_length=50)
    departure_port = models.CharField(max_length=50)
    custom_mex = models.CharField(max_length=50)
    custom_ext = models.CharField(max_length=50)

    def __str__(self):
        return self.description
    
