from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    hp = models.IntegerField()
    torque = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name