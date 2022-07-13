from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Upgrade(models.Model):
    name = models.CharField(max_length=50)
    power = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.price} {self.name}'

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hp = models.IntegerField()
    torque = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for car_id: {self.car_id} @{self.url}'